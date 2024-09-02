import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf
from keras.models import load_model
import streamlit as st


start = '01-01-2022'
end = '31-12-2023'


st.title('Stock Predictor Pro')

user_input = st.text_input('Enter stock Ticker', 'TTML')


df = yf.download(user_input, start=start, end=end)

