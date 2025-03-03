"""
    日経平均株価,ビットコイン、為替の推移をグラフ化する
    5,25,50日移動平均線を追加する
    ボリュームもグラフ化する
    MACDを追加する
    RSIを追加する
    ボリンジャーバンドを追加する
    https://www.youtube.com/watch?v=6R6-BCFd7zM&t=3273s
"""
import pandas as pd
import numpy as np
import talib as ta
import yfinance as yf
import matplotlib.pyplot as plt
import mplfinance as mpf

#start = '2019-07-01';end = '2020-07-01'
#df = yf.download('^N225', start=start, end=end, multi_level_index=None) # Nikkei225
#start = '2020-01-01';end = '2020-107-01'
#df = yf.download('BTC-JPY', start=start, end=end, multi_level_index=None) # BTC-JPY
start = '2020-01-01';end = '2024-12-31'
df = yf.download('USDJPY=X', start=start, end=end, multi_level_index=None)  # USDJPY=X

date = df.index
close = df['Close']
span05=5
span25=25
span50=50

df['sam05'] = close.rolling(window=span05).mean()
df['sam25'] = close.rolling(window=span25).mean()
df['sam50'] = close.rolling(window=span50).mean()

df['macd'], df['macdsignal'], df['macdlist'] = ta.MACD(close, fastperiod=12, slowperiod=26, signalperiod=9) 
df['RSI'] = ta.RSI(close, timeperiod=span25)
df['upper'], df['middle'], df['lower'] = ta.BBANDS(close, timeperiod=span25, nbdevup=2, nbdevdn=2, matype=0)
plt.figure(figsize=(15,10))

plt.subplot(5,1,1)
plt.plot(date,close,label='Nikkei225')
plt.plot(date,df['sam05'],label='sam05',color='y')
plt.plot(date,df['sam25'],label='sam25',color='r')
plt.plot(date,df['sam50'],label='sam50',color='b')
plt.legend()

plt.subplot(5,1,2)
plt.bar(date.values,df['Volume'].values,label='Volume',color='c')
plt.legend()

plt.subplot(5,1,3)
plt.fill_between(date, df['macd'], color='gray', alpha=0.5, label='MACD_hist')
plt.hlines(0, date.min(), date.max(), "gray", linestyles='dashed')    

plt.subplot(5,1,4)
plt.plot(date, df['RSI'], label='RSI', color='gray')
plt.ylim(0, 100)
plt.hlines([30, 50, 70], date.min(), date.max(), "gray", linestyles='dashed')
plt.legend()

plt.subplot(5,1,5)
plt.plot(date,close,label='close', color='#99b898')
plt.fill_between(date, df['upper'], df['lower'], color='gray', alpha=0.3)

plt.legend()
plt.show()

input()