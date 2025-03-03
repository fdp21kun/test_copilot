import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# シンボル設定
symbols = {
    'TOYOTA': '7203.T',  # トヨタ自動車 
    'HONDA': '7267.T',  # ホンダ
}

# データ取得期間
start_date = "2022-01-01" ; end_date = "2025-01-01"

# データ取得
data = {}
for name, symbol in symbols.items():
    data[name] = yf.download(symbol, start=start_date, end=end_date, multi_level_index=None)[['Close']].rename(columns={'Close': name})

# データフレームの統合
merged_data = pd.concat(data.values(), axis=1)

scaling_factor1 = merged_data['TOYOTA'].mean() / merged_data['HONDA'].mean()
merged_data['Scaled#1'] = merged_data['HONDA'] * scaling_factor1
scaling_factor2 = merged_data['HONDA'].mean() / merged_data['TOYOTA'].mean()
merged_data['Scaled#2'] = merged_data['TOYOTA'] * scaling_factor2

print(f"Scaling Factor#1: {scaling_factor1}")
print(f"Scaling Factor#2: {scaling_factor2}")

# 欠損値を削除
merged_data.dropna(inplace=True)

# 相関係数の計算
correlation_matrix = merged_data.corr()

# グラフ作成
plt.figure(figsize=(14, 8))
for column in merged_data.columns:
    plt.plot(merged_data.index, merged_data[column], label=column)

plt.title("Nikkei 225, Dow Jones ETF", fontsize=16)
plt.xlabel("Date", fontsize=12)
plt.ylabel("Value", fontsize=12)
plt.legend(fontsize=12)
plt.grid(True)
plt.tight_layout()
plt.show()

# 相関係数の表示
print("Correlation Matrix:")
print(correlation_matrix)
