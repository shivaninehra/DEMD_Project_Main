# Pulsar Star-Prediction - End to End Deployment using FastAPI and Heroku

## D20031- DEMD End Term Assignment 
The web app has been deployed using FastAPI and Heroku. 

## Problem Statement 
To build a classification model that predicts whether the inputs correspond to a Pulsar Star or not.  Pulsars are a rare type of Neutron star that produce radio emission detectable here on Earth. They are of considerable scientific interest as probes of space-time, the inter-stellar medium, and states of matter. Machine learning tools are now being used to automatically label pulsar candidates to facilitate rapid analysis. Classification systems in particular are being widely adopted,which treat the candidate data sets as binary classification problems.
We have used Class variable as our Target Variable and then deployed the model using Heroku and FastAPI. 

## DataSource 
Link : https://www.kaggle.com/colearninglounge/predicting-pulsar-starintermediate

The dataset is avaiable on Kaggle and has 8 continous variables and a single class variable. The first four are simple statistics obtained from the integrated pulse profile (folded profile). This is an array of continuous variables that describe a longitude-resolved version of the signal that has been averaged in both time and frequency . The remaining four variables are similarly obtained from the DM-SNR curve .
We have further performed EDA and then feature selection to come up with important feature that are essential for this classification problem. 

## Output 
The Heroku app Deployment Link : https://demd-project.herokuapp.com/

All the output screenshots have been uploaded in the Ouput Screenshots Folder. 
