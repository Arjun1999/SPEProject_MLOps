pipeline
{
    agent any
    
    environment {
    
    DOCKER_TAG = getVersion()
    
    }
    
    stages
    {
    
        stage('SCM'){
            steps{
                git credentialsId: 'github', url: 'https://github.com/Arjun1999/SPEProject_MLOps.git'
            }
        }
        
        stage('Train ML Model'){
            steps{
                sh "docker build -t testing-model -f Dockerfile.model ."
                // sh "docker run -d testing-model"
                
            }
        }
        
        // stage('Run Container, Get ID')
        // {
        //     steps{
        //         sh "docker run -d testing-model"
        //     }
            
        //     environment{
        //         CONTAINER_ID = getContainer()
        //     }
        // }
        
        stage ('Remove Container'){
            steps{
                sh "docker rm temp-contain"
            }
        }
        
        stage('Copy Model to Local Directory'){
        
            steps{
                // sh "cd Model1/"
                // sh "ls"
                sh "docker run --name temp-contain -v /var/lib/jenkins/workspace/Flask-Docker-Jenkins-Heroku-Pipeline/Model1/:/app/ testing-model"
                sh "cp Model1/deployment_02062021.pkl ../"
            }
        }
        
        

        stage('Docker Build (App)'){
            steps{
                sh "docker build . -t av99/enigmatic-temple-29693:${DOCKER_TAG}"
            }
        }
        
        
        stage('DockerHub Push (Contribution:p)'){
            steps{
                withCredentials([string(credentialsId: 'docker-hub', variable: 'DockerHubPassword')]) {
                    sh "docker login -u av99 -p ${DockerHubPassword}"
                }
            
                sh "docker push av99/enigmatic-temple-29693:${DOCKER_TAG}"
            }
        }
        
        stage('Deploy to Development'){
            steps{
              withCredentials([usernamePassword(credentialsId: '24f19683-175a-43d8-92f1-c9cd35b3d2fe', passwordVariable: 'HerokuLogin_Password', usernameVariable: 'HerokuLogin_Username')]) {
                    sh "git push https://heroku:${HerokuLogin_Password}@git.heroku.com/spe-fproject.git HEAD:master"
                }
            }
        }
        
        stage('Testing (Test Model API calls)'){
            steps{
                    sh "python testing_predictor.py"
                }
        }
        
        
        stage('Deploy to Production'){
            steps{
              withCredentials([usernamePassword(credentialsId: '24f19683-175a-43d8-92f1-c9cd35b3d2fe', passwordVariable: 'HerokuLogin_Password', usernameVariable: 'HerokuLogin_Username')]) {
                    sh "git push https://heroku:${HerokuLogin_Password}@git.heroku.com/enigmatic-temple-29693.git HEAD:master"
                }
            }
        }
        
        
    }

}


def getVersion()
{
    def commitVersion = sh returnStdout: true, script: 'git rev-parse --short HEAD'
    return commitVersion
}

def getContainer()
{
    def containerID = sh returnStdout: true, script: 'docker ps -aqf "ancestor=testing-model"'
    return containerID
}
