import matplotlib
matplotlib.use('Agg')  # Use a non-GUI backend for Matplotlib

from flask import Flask, render_template, request
import yfinance as yf

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/details', methods=['POST'])
def details():
    # Get user input from the form
    ticker = request.form['ticker']

    # Append '.NS' suffix if needed for NSE stocks
    if not ticker.endswith('.NS'):
        ticker += '.NS'

    try:
        # Fetch stock data
        stock = yf.Ticker(ticker)
        info = stock.info

        if not info:
            return "No data found for the ticker symbol. Please check the symbol and try again."

        # Extract relevant details
        stock_details = {
            "longName": info.get("longName", "N/A"),
            "currentPrice": info.get("currentPrice", "N/A"),
            "previousClose": info.get("previousClose", "N/A"),
            "open": info.get("open", "N/A"),
            "dayLow": info.get("dayLow", "N/A"),
            "dayHigh": info.get("dayHigh", "N/A"),
            "volume": info.get("volume", "N/A"),
            "marketCap": info.get("marketCap", "N/A"),
            "beta": info.get("beta", "N/A"),
            "peRatio": info.get("trailingPE", "N/A"),
            "eps": info.get("trailingEps", "N/A"),
            "earningsDate": info.get("earningsDate", "N/A"),
            "dividendYield": info.get("dividendYield", "N/A"),
            "website": info.get("website", "N/A"),
            "sector": info.get("sector", "N/A"),
            "industry": info.get("industry", "N/A")
        }

        return render_template('details.html', stock_details=stock_details)

    except Exception as e:
        return f"An error occurred: {e}"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')