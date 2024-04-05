import base64
from io import BytesIO

import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
import env
import webbrowser
from flask import Flask, render_template
from StockData import ApiHandler

# Globals
matplotlib.use('Agg')
config = env.Config().config
template_dir = config['TEMPLATE_DIR']
symbol = config['SYMBOL']
historical_date_range = config['HISTORICAL_DATE_RANGE'],
time_interval = config['INTERVAL']

# Initial setup
app = Flask(__name__)
app.template_folder = template_dir
api_handler = ApiHandler.ApiHandler()
pd.set_option('display.max_columns', None)


@app.route('/')
def index():
    # Generate some sample data (replace with real-time stock data)
    x = [1, 2, 3, 4, 5]
    y = [5, 7, 3, 8, 4]

    # Create a simple line plot using Matplotlib
    plt.plot(x, y)
    plt.xlabel('Time')
    plt.ylabel('Price')

    # Save the plot to a BytesIO object
    img = BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)

    # Encode the image to base64
    plot_url = base64.b64encode(img.getvalue()).decode()

    # Close the plot to free memory
    plt.close()

    return render_template('index.html', plot_url=plot_url)


if __name__ == '__main__':
    historical_data = api_handler.fetch_historical_prices()
    print(historical_data)
    # webbrowser.open('http://127.0.0.1:5000/')
    # app.run(debug=True)
