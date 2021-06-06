from flask import Flask,request, url_for, redirect, render_template, jsonify
from pycaret.classification import *
import pandas as pd
import pickle
import numpy as np
import os
import sys

app = Flask(__name__)
port = int(os.environ.get("PORT", 5000))

# load_config('test')
model = load_model(sys.argv[1])
cols = ['RegNo.', 'Quants', 'LogicalReasoning', 'Verbal', 'Programming', 'CGPA', 'Networking', 'CloudComp', 'WebServices', 'DataAnalytics', 'QualityAssurance', 'AI']

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/predict',methods=['POST'])
def predict():
    int_features = [x for x in request.form.values()]
    final = np.array(int_features)
    data_unseen = pd.DataFrame([final], columns = cols)
    prediction = predict_model(model, data=data_unseen)
    prediction = int(prediction.Label[0])

    if(prediction == 1):
        pred_str = "Congratulation! You are on track and good to go :)"
    else:
        pred_str = "Sorry :( You're not there yet but keep on going!"
    
    # return render_template('home.html',pred = 'Expecteddd Bill will be {}'.format(prediction))
    return render_template('home.html',pred = pred_str)

@app.route('/predict_api',methods=['POST'])
def predict_api():
    data = request.get_json(force=True)
    data_unseen = pd.DataFrame([data])
    prediction = predict_model(model, data=data_unseen)
    output = prediction.Label[0]
    return jsonify(output)

if __name__ == '__main__':
    
    app.run(port = port, debug=True, host='0.0.0.0')
    