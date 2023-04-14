import json
import pandas as pd
import requests
import os

def get_csv_from_api(stock_symbol):
    api_key = os.environ.get('ALPHA_VANTAGE_API_KEY')
    url = f'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={stock_symbol}&interval=5min&apikey={api_key}'

    r = requests.get(url)
    data = r.json()

    time_series = data['Time Series (5min)']

    # Convert the JSON data to a pandas DataFrame
    data = []
    for timestamp, values in time_series.items():
        row = {'Timestamp': timestamp}
        row.update(values)
        data.append(row)

    df = pd.DataFrame(data)

    # Rename columns
    df.rename(columns={'1. open': 'Open', '2. high': 'High', '3. low': 'Low', '4. close': 'Close', '5. volume': 'Volume'}, inplace=True)

    # Export DataFrame to CSV
    return df.to_csv(index=False)