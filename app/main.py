# train_model.py
import requests
import pandas as pd
from sklearn.linear_model import LinearRegression
import joblib

url = "https://api.coingecko.com/api/v3/coins/bitcoin/ohlc?vs_currency=usd&days=1"
headers = {
    "x-cg-demo-api-key": "CG-7pi9DCcf6E6PmCFBLrwvGtZT"
}

res = requests.get(url, headers=headers)
data = res.json()

df = pd.DataFrame(data, columns=["timestamp", "open", "high", "low", "close"])
df["timestamp"] = pd.to_datetime(df["timestamp"], unit="ms")

# Fitur dan target
X = df[["open", "high", "low"]]
y = df["close"]

model = LinearRegression()
model.fit(X, y)

joblib.dump(model, "model/price_model.pkl")
print("Model saved!")
