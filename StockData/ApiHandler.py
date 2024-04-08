import json
import yfinance
import requests
import pandas as pd


class ApiHandler:

    @staticmethod
    def fetch_historical_prices(symbol):
        historical_data = {}
        apple_data = yfinance.Ticker(symbol)
        last_fourteen_close = pd.DataFrame(apple_data.history(period="14d"))

        for index, row in last_fourteen_close.iterrows():
            date = index.strftime("%Y-%m-%d")
            close_price = row['Close']
            historical_data[date] = close_price

        return pd.DataFrame.from_dict(historical_data, orient='index', columns=['Prices'])

    @staticmethod
    def fetch_current_price(SYMBOL, API_KEY):
        url = f'https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={SYMBOL}&apikey={API_KEY}'
        response = requests.get(url)
        data = response.json()
        print(data)
        return float(data['Global Quote']['05. price'])
