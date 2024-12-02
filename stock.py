import yfinance as yf
import pandas as pd
import schedule
import time

def fetch_stock_data(ticker, start_date, end_date, file_name=None):
    stock_data = yf.download(ticker, start=start_date, end=end_date, interval='1d')
    
    print("Head of the DataFrame:")
    print(stock_data.head())
    
    if file_name:
        stock_data.to_csv(file_name, index=True)
        print(f"Data saved to {file_name}")
    
    return stock_data

stock_data = fetch_stock_data('AAPL', '2023-01-01', '2024-12-01', file_name='stock_data.csv')
print(stock_data)
