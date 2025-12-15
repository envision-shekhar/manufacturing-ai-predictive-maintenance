
# src/api.py
from fastapi import FastAPI
from pydantic import BaseModel
import os, pickle
import numpy as np

MODEL_PATH = os.environ.get('MODEL_PATH', 'models/kiln_model.pkl')
app = FastAPI(title='Kiln Predictive Maintenance API')

class Sample(BaseModel):
    temperature: float
    pressure: float
    vibration: float
    o2: float
    co: float
    airflow: float
    setpoint_dev: float
    wear_index: float
    humidity: float
    feed_rate: float

with open(MODEL_PATH, 'rb') as f:
    model = pickle.load(f)

@app.get('/health')
def health():
    return {'status': 'ok'}

@app.post('/predict')
def predict(s: Sample):
    x = np.array([[s.temperature, s.pressure, s.vibration, s.o2, s.co, s.airflow, s.setpoint_dev, s.wear_index, s.humidity, s.feed_rate]])
    y = model.predict(x)[0]
    return {'failure': int(y)}
