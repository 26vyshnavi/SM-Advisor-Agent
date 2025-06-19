from alpha_vantage.timeseries import TimeSeries
import os
from dotenv import load_dotenv

load_dotenv()

ALPHA_KEY = os.getenv('ALPHA_VANTAGE_KEY')

def fetch_stock_data(symbol):
    ts = TimeSeries(key=ALPHA_KEY)
    data, meta_data = ts.get_daily(symbol=symbol)
    latest_date = sorted(data.keys())[-1]
    latest_data = data[latest_date]
    return {
        "date": latest_date,
        "open": latest_data["1. open"],
        "high": latest_data["2. high"],
        "low": latest_data["3. low"],
        "close": latest_data["4. close"],
        "volume": latest_data["5. volume"]
    }

# Example usage:
print(fetch_stock_data("AAPL"))