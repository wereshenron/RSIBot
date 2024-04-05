import json
import yfinance
import requests


class ApiHandler:

    @staticmethod
    def fetch_historical_prices():
        historical_data = {}
        get_apple_data = yfinance.Ticker('AAPL')
        last_five_close = get_apple_data.history(period="5d")['Close']
        print(last_five_close)
        # return historical_prices

    @staticmethod
    def fetch_current_price(SYMBOL, API_KEY):
        url = f'https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={SYMBOL}&apikey={API_KEY}'
        response = requests.get(url)
        data = response.json()
        print(data)
        return float(data['Global Quote']['05. price'])
