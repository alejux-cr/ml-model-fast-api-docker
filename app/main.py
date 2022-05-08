import pickle
import numpy as np
from fastapi import FastAPI
from pydantic import BaseModel, conlist
from typing import List


app = FastAPI(title="Wine Class Prediction")

# Represents a particular wine (or datapoint)
class Wine(BaseModel):
  alcohol: float
  malic_acid: float
  ash: float
  alcalinity_of_ash: float
  magnesium: float
  total_phenols: float
  flavanoids: float
  nonflavanoid_phenols: float
  proanthocyanins: float
  color_intensity: float
  hue: float
  od280_od315_of_diluted_wines: float
  proline: float
  batches: List[conlist(item_type=float, min_items=13, max_items=13)]


@app.on_event("startup")
def load_clf():
  # Load classifier into memory from pickle file for prediction
  with open("/app/wine.pkl", "rb") as file:
    global clf
    clf = pickle.load(file)


@app.get("/")
def home():
  return "Congratulations! Your API is working as expected. Now head over to http://localhost:8000/docs"


@app.post("/predict")
def predict(wine: Wine):
  batches = wine.batches
  np_batches = np.array(batches)
  pred = clf.predict(np_batches).tolist()

  return {"Predictions": pred}
