# app/model.py
import joblib
from app.utils import get_latest_ohlc

model = joblib.load("model/price_model.pkl")

def predict_close_price():
    features = get_latest_ohlc()
    pred = model.predict([features])[0]
    return round(pred, 2)
