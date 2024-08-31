import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf
from keras.models import load_model
import streamlit as st


start = '2010-01-01'
end = '2024-07-28'


st.title('Stock Predictor Pro')

user_input = st.text_input('Enter stock Ticker', 'AAPL')


df = yf.download(user_input, start=start, end=end)

# Describe the data
st.subheader('Date from 2010-2024')
st.write(df.describe())


