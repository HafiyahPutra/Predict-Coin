from fastapi import FastAPI
import joblib
import pandas as pd
import requests

app = FastAPI()

# Load model
model = joblib.load("model/price_model.pkl")

# Endpoint untuk prediksi
@app.get("/predict")
def predict():
    # Ambil data dari CoinGecko OHLC API
    url = "https://api.coingecko.com/api/v3/coins/bitcoin/ohlc?vs_currency=usd&days=1"
    headers = {"x-cg-demo-api-key": "CG-7pi9DCcf6E6PmCFBLrwvGtZT"}
    response = requests.get(url, headers=headers)
    ohlc_data = response.json()

    # Ambil bar terakhir (data terbaru)
    latest = ohlc_data[-1]  # [timestamp, open, high, low, close]
    features = pd.DataFrame([latest[1:5]], columns=["open", "high", "low", "close"])

    # Prediksi
    prediction = model.predict(features)[0]
    return {"predicted_price": prediction}
