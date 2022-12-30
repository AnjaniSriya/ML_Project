import warnings
warnings.filterwarnings('ignore')  # Hide warnings
import datetime as dt
import pandas as pd
pd.core.common.is_list_like = pd.api.types.is_list_like
import pandas_datareader.data as web
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from plotly import graph_objs as go

from PIL import Image
import os

from mpl_finance import candlestick_ohlc
import matplotlib.dates as mdates
import streamlit as st


#Importing Libraries done

#title
st.title('Stock Market App')
'---------------------------------------------------------'

st.progress(100)

st.header('Give us input :D')
com = st.file_uploader("Choose a file")
if com is not None:
    # Can be used wherever a "file-like" object is accepted:
    dataframe = pd.read_csv(com)

df = dataframe # Collects data
df.reset_index(inplace=True)
df.set_index("Date", inplace=True)

high = df['High'].mean()
low = df['Low'].mean()
avg = df['VWAP'].mean()
avgprevclose = df['Prev Close'].mean()
avgopen = df['Open'].mean()
avgvol = df['Volume'].mean()

st.subheader("Enter Present Stock Value:")
num= st.number_input("Stock value:")

st.markdown('**The entered stock value is:**')
num

st.subheader("Our Recommendation:")

if num > high:
    st.info("Not suggestable")
elif num > avg:
    if num < high:
        st.info("Depends on the type investments you choose")
elif num < avg:
    if num > low:
        st.info("Yayyy! you can invest. Good Luck!")
        if avgopen < avgprevclose:
            st.info("Yayyy! you can invest. Good Luck!")
    else:
        st.info("There is chance for market to not recover. Try to invest when it's likely to improve.")


st.subheader("Reference graphs")

'1. The Stock Open Values over time: '
st.line_chart(df["Open"])

'2. The Stock Close Values over time: '
st.line_chart(df["Close"])
