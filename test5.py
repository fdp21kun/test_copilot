import yfinance as yf

# 日経225先物のティッカー
ticker = "NIY=F"

# データ取得期間
start_date = "2022-01-01"
end_date = "2025-01-01"

# データ取得
nikkei_futures = yf.download(ticker, start=start_date, end=end_date, multi_level_index=None)

# 結果の表示
print(nikkei_futures.head())
print("....")
print(nikkei_futures.tail())
