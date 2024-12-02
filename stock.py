import yfinance as yf
import pandas as pd
import schedule
import time
from datetime import datetime

def fetch_stock_data(ticker, start_date, end_date, file_name=None):
    #valid intervals: [1m, 2m, 5m, 15m, 30m, 60m, 90m, 1h, 1d, 5d, 1wk, 1mo, 3mo]
    stock_data = yf.download(ticker, start=start_date, end=end_date, interval='1wk')
    
    print("Head of the DataFrame:")
    print(stock_data.head())
    
    if file_name:
        stock_data.to_csv(file_name, index=True)
        print(f"Data saved to {file_name}")
    
    return stock_data

today = datetime.now().date()
print(today)

    

stock_data = fetch_stock_data('AAPL', '2023-01-01', today, file_name='stock_data.csv')
#print(stock_data)
