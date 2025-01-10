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

start = '2024-09-01';end = '2025-01-10'
df = yf.download('^N225', start=start, end=end, multi_level_index=None) # Nikkei225
df['upper'], df['middle'], df['lower'] = ta.BBANDS(df['Close'], timeperiod=25, nbdevup=2, nbdevdn=2, matype=0)
df['macd'], df['macdsignal'], df['macdhist'] = ta.MACD(df['Close'], fastperiod=12, slowperiod=26, signalperiod=9) 
df['RSI'] = ta.RSI(df['Close'], timeperiod=25)

adps = [
    mpf.make_addplot(df['upper'],    color='g'), 
    mpf.make_addplot(df['middle'],   color='b'), 
    mpf.make_addplot(df['lower'],    color='r'),
    mpf.make_addplot(df['macdhist'], color='dimgray', type='bar', width=1.0, panel=1, alpha=0.5, ylabel='MACD'),
    mpf.make_addplot(df['RSI'],      type='line', width=1.0, panel=2, ylabel='RSI'),
]
mpf.plot(df, type='candle', figsize=(15, 10), style='yahoo', volume=True, addplot=adps, volume_panel=3, panel_ratios=(5, 2, 2, 1))
input()