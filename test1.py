import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime

def fetch_stock_data_from_nse(symbol):
    # URL for NSE stock data
    url = f"https://www.nseindia.com/get-quotes/equity?symbol={symbol}"
    
    # Send HTTP request
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}
    response = requests.get(url, headers=headers)
    
    # Check if the request was successful
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Extract stock data from the page
        # Note: You might need to inspect the page to find the correct HTML elements
        data = {}
        for div in soup.find_all("div", class_="col-xs-12 col-sm-12 col-md-4 col-lg-4"):
            span = div.find("span", class_="value")
            if span:
                label = div.find("div", class_="label").get_text(strip=True)
                value = span.get_text(strip=True)
                data[label] = value

        return data
    else:
        print(f"Failed to retrieve data: HTTP {response.status_code}")
        return None

# Define the stock ticker symbol
symbol = 'TTML'

# Fetch stock data
stock_data = fetch_stock_data_from_nse(symbol)

# Print the stock data
if stock_data:
    for key, value in stock_data.items():
        print(f"{key}: {value}")
else:
    print("No data available")
