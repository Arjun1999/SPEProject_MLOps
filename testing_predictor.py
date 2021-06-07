import requests
import json
# Test the ML models in the application through their respective API calls

url = 'https://spe-fproject.herokuapp.com/predict_api'


pred = requests.post(url, json={'RegNo.':'T150054399', 'Quants':25, 'LogicalReasoning':25, 'Verbal':25, 'Programming':25, 'CGPA':10, 'Networking':10, 'CloudComp':10, 'WebServices':10, 'DataAnalytics':10, 'QualityAssurance':10, 'AI':10})
print(pred.json())







# For regression model
# pred = requests.post(url,json={'age':55, 'sex':'male', 'bmi':59, 'children':1, 'smoker':'male', 'region':'northwest'})
# print(pred.json())

