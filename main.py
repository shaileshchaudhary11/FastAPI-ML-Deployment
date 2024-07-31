# main.py
from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
import joblib
import numpy as np

# Load the trained model
model = joblib.load('iris_model.pkl')

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to the Iris Prediction API"}

@app.get("/model-info/")
def model_info():
    return {"model": "RandomForestClassifier", "version": "1.0"}

# Define the request body
class IrisFeatures(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float

@app.post("/predict/")
def predict(iris: IrisFeatures):
    data = np.array([[
        iris.sepal_length,
        iris.sepal_width,
        iris.petal_length,
        iris.petal_width
    ]])
    prediction = model.predict(data)
    return {"prediction": int(prediction[0])}
