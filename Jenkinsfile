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
        
        // // stage('Run Container, Get ID')
        // // {
        // //     steps{
        // //         sh "docker run -d testing-model"
        // //     }
            
        // //     environment{
        // //         CONTAINER_ID = getContainer()
        // //     }
        // // }
        
        stage ('Remove Container'){
            steps{
                sh "docker rm temp-contain"
            }
        }
        
        
        stage('Copy Model to Jenkins Workspace'){
        
            steps{
                // sh "cd Model1/"
                // sh "ls"
                sh "docker run --name temp-contain -v /var/lib/jenkins/workspace/Flask-Docker-Jenkins-Heroku-Pipeline/Model2/:/app/ testing-model"
                sh 'cp /var/lib/jenkins/workspace/Flask-Docker-Jenkins-Heroku-Pipeline/Model2/deployment_05062021.pkl /var/lib/jenkins/workspace/Flask-Docker-Jenkins-Heroku-Pipeline/'
                
            }
        }
        
        stage('SSH and Copy to Local Machine'){
            steps{
                sh 'scp -v -o StrictHostKeyChecking=no deployment_05062021.pkl arjun@172.17.0.1:/home/arjun/Desktop/Semester_8/SPE/FinalProject/'
            }
        }

        stage('Docker Build (App)'){
            steps{
                sh "docker build . -t av99/enigmatic-temple-29693:${DOCKER_TAG}"
            }
        }
        
        
        stage('DockerHub Push (Contribution to OpenSource :p)'){
            steps{
                withCredentials([string(credentialsId: 'docker-hub', variable: 'DockerHubPassword')]) {
                    sh "docker login -u av99 -p ${DockerHubPassword}"
                }
            
                sh "docker push av99/enigmatic-temple-29693:${DOCKER_TAG}"
            }
        }
        
        stage('Deploy to Development'){
            steps{
                    sh 'git config --global user.email jenkins@172.17.0.1'
                    sh 'git config --global user.name jenkins'
                    
              withCredentials([usernamePassword(credentialsId: '24f19683-175a-43d8-92f1-c9cd35b3d2fe', passwordVariable: 'HerokuLogin_Password', usernameVariable: 'HerokuLogin_Username')]) {
                    
                    sh 'git add .'
                    sh 'git commit -m "New Model Loaded" '
          
                    sh "git push https://heroku:${HerokuLogin_Password}@git.heroku.com/spe-fproject.git HEAD:master"
                }
            }
        }
        
        // stage('Deploy to Development'){
        //     steps{
        //             withCredentials([usernamePassword(credentialsId: 'github', passwordVariable: 'github_pwd', usernameVariable: 'github_user'), usernamePassword(credentialsId: '24f19683-175a-43d8-92f1-c9cd35b3d2fe', passwordVariable: 'heroku_pwd', usernameVariable: 'heroku_user')])
        //             {  
        //                     sh 'git add .'
        //                     sh 'sudo git commit -m "New Model Loaded" '
        //                     sh "git push https://heroku:${HerokuLogin_Password}@git.heroku.com/spe-fproject.git HEAD:master"
        //             }
    
        //     }
        // }
        
        
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
