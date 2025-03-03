import yfinance as yf

# ティッカーシンボル（例：日経225 ETF）
ticker = "SPY"

# ティッカーのオプションデータ
stock = yf.Ticker(ticker)

# 有効なオプション満期日を確認
print(stock.options)

# 特定の満期日のオプションデータを取得
opt = stock.option_chain(date='2025-01-22')
print(opt.calls)  # コールオプション
print(opt.puts)   # プットオプション
