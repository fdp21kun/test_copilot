"""
    mplfinanceを使って日経平均株価,ボリンジャーバンドをグラフ化する
    https://www.youtube.com/watch?v=6R6-BCFd7zM&t=3273s
"""
import pandas as pd
import numpy as np
import talib as ta
import yfinance as yf
import matplotlib.pyplot as plt
import mplfinance as mpf

start = '2019-07-01';end = '2020-07-01'
df = yf.download('^N225', start=start, end=end, multi_level_index=None) # Nikkei225

date = df.index
close = df['Close']
span05=5
span25=25
span50=50

df['upper'], df['middle'], df['lower'] = ta.BBANDS(close, timeperiod=span25, nbdevup=2, nbdevdn=2, matype=0)
df_candle = df[['High', 'Low', 'Open', 'Close', 'Volume']]

tcdf = df[['upper', 'middle', 'lower']]
apd = mpf.make_addplot(tcdf)
mpf.plot(df_candle, addplot=apd, type='candle', volume=True, style='yahoo', figsize=(15, 10))


input()