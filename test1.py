import streamlit as st
import yfinance as yf
import pandas as pd

# タイトル
st.title('日本株表示アプリケーション')

# 銘柄コードの入力
ticker = st.text_input('銘柄コードを入力してください (例: 7203.T for Toyota)', '7203.T')

# データ取得
if ticker:
    stock_data = yf.Ticker(ticker)
    df = stock_data.history(period='1d', start='2020-1-1', end='2023-12-31')

    # 株価データの表示
    st.write(f'{ticker} の株価データ')
    st.line_chart(df['Close'])

    # データフレームの表示
    st.write('データフレーム')
    st.dataframe(df)
else:
    print("株価取得失敗")