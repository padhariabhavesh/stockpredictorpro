import matplotlib
matplotlib.use('Agg')  # Use a non-GUI backend for Matplotlib

from flask import Flask, render_template, request, jsonify
import yfinance as yf
from datetime import datetime

app = Flask(__name__)

# In-memory storage for users (replace this with a database in a real app)
users = []

@app.route('/')
def home():
    return render_template('index.html')  # Stock search page

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        registration_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        # Check if email already exists
        if any(user['email'] == email for user in users):
            return "Email already exists. Please log in."

        # Add new user
        users.append({'username': username, 'email': email, 'password': password, 'date': registration_date})
        
        # Redirect to login page after successful signup
        return redirect(url_for('login'))

    return render_template('signup.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        # Check if user exists
        user = next((user for user in users if user['email'] == email and user['password'] == password), None)
        if user:
            return redirect(url_for('home'))
        else:
            return "Invalid email or password."

    return render_template('login.html')

@app.route('/admin')
def admin():
    return render_template('admin.html', users=users)

@app.route('/details', methods=['POST'])
def details():
    ticker = request.form['ticker']

    if not ticker.endswith('.NS'):
        ticker += '.NS'

    try:
        stock = yf.Ticker(ticker)
        info = stock.info
        history = stock.history(period="1y")  # Fetch 1 year of historical data

        if not info:
            return "No data found for the ticker symbol. Please check the symbol and try again."

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
            "industry": info.get("industry", "N/A"),
            "history": history.reset_index().to_dict(orient='records')  # Convert history to dict
        }

        return render_template('details.html', stock_details=stock_details)

    except Exception as e:
        return f"An error occurred: {e}"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
