# app/utils.py
import requests

def get_latest_ohlc():
    url = "https://api.coingecko.com/api/v3/coins/bitcoin/ohlc?vs_currency=usd&days=1"
    headers = {"x-cg-demo-api-key": "CG-7pi9DCcf6E6PmCFBLrwvGtZT"}
    res = requests.get(url, headers=headers)
    data = res.json()

    latest = data[-1]
    return [latest[1], latest[2], latest[3]]  # open, high, low
