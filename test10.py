import yfinance as yf

# ティッカーを指定
ticker = "94345.T"

try:
    # データ取得
    data = yf.download(ticker, start="2022-01-01", end="2025-01-01")
    if data.empty:
        print(f"No data found for ticker: {ticker}")
    else:
        print(data.head())
except Exception as e:
    print(f"Error fetching data for ticker {ticker}: {e}")
