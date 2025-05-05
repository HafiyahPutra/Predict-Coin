from fastapi import FastAPI
import joblib
import pandas as pd
import requests
import os

app = FastAPI()

# Load model
model_path = os.path.join("model", "price_model.pkl")
model = joblib.load(model_path)

@app.get("/")
def root():
    return {"message": "Predict-Coin is running."}

@app.get("/predict")
def predict():
    try:
        # Ambil data dari API
        url = "https://api.coingecko.com/api/v3/coins/bitcoin/ohlc?vs_currency=usd&days=1"
        headers = {"x-cg-demo-api-key": "CG-7pi9DCcf6E6PmCFBLrwvGtZT"}
        response = requests.get(url, headers=headers)
        data = response.json()

        # Ambil data terakhir
        last = data[-1]  # Format: [timestamp, open, high, low, close]
        df = pd.DataFrame([last[1:5]], columns=["open", "high", "low"])

        # Prediksi
        pred = model.predict(df)[0]
        return {"predicted_price": pred}
    except Exception as e:
        return {"error": str(e)}
