from flask import Flask, request
import numpy as np
import pandas as pd
import pickle
from flasgger import Swagger

app = Flask(__name__)

#loading model using pickle file
pickle_file_open = open("Pulsar_star_pickle.pkl")
classifier = pickle.load(pickle_file_open)

@app.route('/', methods =["GET"])
def welcome_message():
    try:
        return "Welcome to Praxis", 200
    except:
        return "Something went wrong", 400

@app.route('/predict', methods= ["GET"])
def predict():
    meanIntProfile = request.args.get("Mean of the integrated profile")
    stdIntProfile = request.args.get("Standard deviation of the integrated profile")
    skewIntProfile = request.args.get("Skewness of the integrated profile")
    meanDMSNR = request.args.get("Mean of the DM-SNR curve")
    excKurtDMSNR = request.args.get("Excess kurtosis of the DM-SNR curve")
    result = classifier.predict([[meanIntProfile,stdIntProfile,skewIntProfile,meanDMSNR,excKurtDMSNR]])
    if result in [0,"0"]: return "Not a Pulsar Star",200
    return "Valid Pulsar Star",200
