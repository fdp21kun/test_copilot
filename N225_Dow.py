import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# シンボル設定
symbols = {
#    'Nikkei': '^N225',  # 日経平均株価
#    'Dow': '^DJI',      # ダウ平均株価
#    'DowETF1': '1546.T',  # ダウETF#1, N225ETFとの相関0.963996
#    'DowETF2': '2846.T',  # ダウETF#2 N225ETFとの相関0.837673
    'USD/JPY': 'USDJPY=X',  # 為替（USD/JPY）
    'N225ETF': '1321.T',  # 日経ETF
#    'SP500ETF': '1655.T',  # S&P500ETF N225ETFとの相関0.966652
#    'TOPICSETF': '1306.T',  # トピックスETF N225ETFとの相関0.995000
}

# データ取得期間
start_date = "2022-01-01"
end_date = "2025-01-01"

# データ取得
data = {}
for name, symbol in symbols.items():
    data[name] = yf.download(symbol, start=start_date, end=end_date, multi_level_index=None)[['Close']].rename(columns={'Close': name})

# データフレームの統合
merged_data = pd.concat(data.values(), axis=1)

# 225 を Dow に重ねるための動的スケーリング係数の計算（平均値の比率を使用）
# scaling_factor1 = merged_data['N225ETF'].mean() / merged_data['DowETF1'].mean()
# merged_data['Scaled#1'] = merged_data['DowETF1'] * scaling_factor1
# scaling_factor2 = merged_data['DowETF1'].mean() / merged_data['N225ETF'].mean()
# merged_data['Scaled#2'] = merged_data['N225ETF'] * scaling_factor2

# scaling_factor1 = merged_data['N225ETF'].mean() / merged_data['DowETF2'].mean()
# merged_data['Scaled#1'] = merged_data['DowETF2'] * scaling_factor1
# scaling_factor2 = merged_data['DowETF2'].mean() / merged_data['N225ETF'].mean()
# merged_data['Scaled#2'] = merged_data['N225ETF'] * scaling_factor2

scaling_factor1 = merged_data['N225ETF'].mean() / merged_data['USD/JPY'].mean()
merged_data['Scaled#1'] = merged_data['USD/JPY'] * scaling_factor1
scaling_factor2 = merged_data['USD/JPY'].mean() / merged_data['N225ETF'].mean()
merged_data['Scaled#2'] = merged_data['N225ETF'] * scaling_factor2

# scaling_factor1 = merged_data['N225ETF'].mean() / merged_data['SP500ETF'].mean()
# merged_data['Scaled#1'] = merged_data['SP500ETF'] * scaling_factor1
# scaling_factor2 = merged_data['SP500ETF'].mean() / merged_data['N225ETF'].mean()
# merged_data['Scaled#2'] = merged_data['N225ETF'] * scaling_factor2

# scaling_factor1 = merged_data['SP500ETF'].mean() / merged_data['DowETF1'].mean()
# merged_data['Scaled#1'] = merged_data['DowETF1'] * scaling_factor1
# scaling_factor2 = merged_data['DowETF1'].mean() / merged_data['SP500ETF'].mean()
# merged_data['Scaled#2'] = merged_data['SP500ETF'] * scaling_factor2

#scaling_factor1 = 14.0
#scaling_factor1 = merged_data['N225ETF'].mean() / merged_data['TOPICSETF'].mean()
#merged_data['Scaled#1'] = merged_data['TOPICSETF'] * scaling_factor1
#scaling_factor2 = merged_data['TOPICSETF'].mean() / merged_data['N225ETF'].mean()
#merged_data['Scaled#2'] = merged_data['N225ETF'] * scaling_factor2

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
