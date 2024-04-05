import os


class Config:
    config = {
        'TEMPLATE_DIR': os.path.abspath(os.path.join(os.path.dirname(__file__), 'Resources', 'views')),
        'HISTORICAL_DATE_RANGE': 14,
        'INTERVAL': 'daily',
        'CLIENT_ID': 'dj0yJmk9UTlOZlRSbWdFUGU5JmQ9WVdrOVlVWjRNSFJoTWtRbWNHbzlNQT09JnM9Y29uc3VtZXJzZWNyZXQmc3Y9MCZ4PTg2',
        'CLIENT_SECRET': 'b8d1ec62c8df3037f23fe5f6c28662fc5ebe3541',
        'SYMBOL': 'AAPL'
    }
