import pandas as pd
import streamlit as st
import yfinance as yf
import math as m
#streamlit run app.py
data=['ABBOTINDIA.NS','ALKEM.NS','ASIANPAINT.NS',
      'BAJAJ-AUTO.NS','BATAINDIA.NS','BERGEPAINT.NS',
      'BHARTIARTL.NS','BRITANNIA.NS','CIPLA.NS','COLPAL.NS',
      'DABUR.NS','DRREDDY.NS','HCLTECH.NS','HDFCBANK.NS',
      'HINDUNILVR.NS','ITC.NS','INFY.NS','LT.NS','MRF.NS',
      'MARICO.NS','NESTLEIND.NS','PVRINOX.NS','PAGEIND.NS',
      'PIDILITIND.NS','POWERGRID.NS','SBILIFE.NS','SUNPHARMA.NS',
      'TCS.NS','TITAN.NS','TORNTPHARM.NS','ULTRACEMCO.NS','UBL.NS']
df=pd.DataFrame(data,columns=['Stocks'])
st.write("PRICE CALCULATOR")
stock = st.selectbox("Choose Stocks",df['Stocks'])
num_days = st.selectbox("Number of Days till expiry",list(range(1, 30)))
df2 =yf.download(stock,period='5y',interval='1d',progress=False)
df2['Returns'] = df2.Close.pct_change() #calculate log retruns
sd = df2.Returns.std(skipna=True) #calculate Std dev calc for daily prices
Current_price=round(df2['Close'].iloc[-1])#get current price
Call_strike = round(Current_price + sd*m.sqrt((num_days))*Current_price) #calculate Call strike based on select
Put_strike = round(Current_price - sd*m.sqrt(num_days)*Current_price) #calculate put strike based on seleted number of days
st.write("CE Strike:",Call_strike)
st.write("PE Strike:",Put_strike)
