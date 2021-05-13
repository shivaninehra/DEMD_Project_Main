<<<<<<< HEAD
#library imports 
import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel
from PulsarStar import PulsarStars
import os
import numpy as np 
import pickle
import pandas as pd 

# create teh app object 
app = FastAPI()
pulsar_star_model = open("Pulsar_star_pickle.pkl","rb")
model = pickle.load(pulsar_star_model) # to load the pickle file

#index route opens automatically at http://127.0.0.1:8000
@app.get('/')
def index():
    return {"message":"Hello Builder"}

#route with a single paramater returns the parameter within a message
#located at http://127.0.0.1:8000/AnyNameHere
@app.get('/{name}')
def get_name(name: str):
    return {"message": f'hello, {name}'}

#expose the prediction functionality,  make the prediction based on the passed
#JSON data and return the predicted Pulsar Star with the confidence
@app.post('/predict')
def Pulsar_Star(data:PulsarStars):
    data = data.dict()
    meanintprofile = data['meanintprofile']
    stdintprofile = data['stdintprofile']
    skewintprofile = data['skewintprofile']
    meandmsnr = data['meandmsnr']
    exckurtdmsnr = data['exckurtdmsnr']
    prediction = model.predict([[meanintprofile,stdintprofile,skewintprofile,meandmsnr,exckurtdmsnr]])
    return {"If prediction is 0 , then its not a pulsar Star. Else Pulsar star ": f'Prediction, {prediction}'}
    #if(prediction[0] > 0.5):
    #    prediction="Not a Pulsar Star"
   # else: 
   #     prediction="Its a Pulsar Star"
    #return {
    #    'prediction': prediction
  #  }

#5. Run the API with uvicorn
# will run on http://127.0.0.1:8000
if __name__ == "__main__":
    uvicorn.run(app,host='127.0.0.1',port=8000)

=======
#library imports 
import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel
from PulsarStar import PulsarStars
import os
import numpy as np 
import pickle
import pandas as pd 

# create teh app object 
app = FastAPI()
pulsar_star_model = open("Pulsar_star_pickle.pkl","rb")
model = pickle.load(pulsar_star_model) # to load the pickle file

#index route opens automatically at http://127.0.0.1:8000
@app.get('/')
def index():
    return {"message":"Hello Builder"}

#route with a single paramater returns the parameter within a message
#located at http://127.0.0.1:8000/AnyNameHere
@app.get('/{name}')
def get_name(name: str):
    return {"message": f'hello, {name}'}

#expose the prediction functionality,  make the prediction based on the passed
#JSON data and return the predicted Pulsar Star with the confidence
@app.post('/predict')
def Pulsar_Star(data:PulsarStars):
    data = data.dict()
    meanintprofile = data['meanintprofile']
    stdintprofile = data['stdintprofile']
    skewintprofile = data['skewintprofile']
    meandmsnr = data['meandmsnr']
    exckurtdmsnr = data['exckurtdmsnr']
    prediction = model.predict([[meanintprofile,stdintprofile,skewintprofile,meandmsnr,exckurtdmsnr]])
    return {"If prediction is 0 , then its not a pulsar Star. Else Pulsar star ": f'Prediction, {prediction}'}
    #if(prediction[0] > 0.5):
    #    prediction="Not a Pulsar Star"
   # else: 
   #     prediction="Its a Pulsar Star"
    #return {
    #    'prediction': prediction
  #  }

#5. Run the API with uvicorn
# will run on http://127.0.0.1:8000
if __name__ == "__main__":
    uvicorn.run(app,host='0.0.0.0',port=5000)

>>>>>>> 3916701 (Fourth Commit)
#uvicorn app:app --reload