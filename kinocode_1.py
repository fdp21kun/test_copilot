"""
    日経平均株価の推移をグラフ化する
    5,25,50日移動平均線を追加する
    2020/06/01～2021/06/01のデータを取得する
    ボリュームもグラフ化する
"""
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

start = '2019-06-01'
end = '2020-06-01'

df = yf.download('^N225', start=start, end=end, multi_level_index=None)
date = df.index
price = df['Close']
span01=5
span02=25
span03=50

df['sam05'] = price.rolling(window=span01).mean()
df['sam25'] = price.rolling(window=span02).mean()
df['sam50'] = price.rolling(window=span03).mean()

plt.figure(figsize=(10,5))
plt.title('Ni225',color='blue',backgroundcolor='white',size=20,loc='center')

plt.subplot(2,1,1)
plt.xlabel('date',color='black',size=10)
plt.ylabel('price',color='black',size=10)
plt.plot(date,price,label='Nikkei225')
plt.plot(date,df['sam05'],label='sam05',color='y')
plt.plot(date,df['sam25'],label='sam25',color='r')
plt.plot(date,df['sam50'],label='sam50',color='b')
plt.legend()

plt.subplot(2,1,2)
plt.bar(date.values,df['Volume'].values,label='Volume',color='c')

plt.legend()
plt.show()

input()