import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# シンボル設定
symbols = {
#    'Nikkei': '^N225',  # 日経平均株価
#    'Dow': '^DJI',      # ダウ平均株価
#    'DowETF1': '1546.T',  # ダウETF#1, N225ETFとの相関0.963996
#    'DowETF2': '2846.T',  # ダウETF#2 N225ETFとの相関0.837673
#    'USD/JPY': 'USDJPY=X',  # 為替（USD/JPY）
    'N225ETF': '1321.T',  # 日経ETF
#    'SP500ETF': '1655.T',  # S&P500ETF N225ETFとの相関0.966652
    'TOPICSETF': '1306.T',  # トピックスETF N225ETFとの相関0.995000
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

# Topics を 225 に重ねるための動的スケーリング係数を 14 で計算
scaling_factor1 = 14.0
merged_data['Scaled#1'] = merged_data['TOPICSETF'] * scaling_factor1

# 欠損値を削除
merged_data.dropna(inplace=True)

# トピックスETF * 14 と日経ETFの差を計算
merged_data['diff_data'] = merged_data['Scaled#1'] - merged_data['N225ETF']

# 相関係数の計算
correlation_matrix = merged_data.corr()

# グラフ作成
plt.figure(figsize=(14, 8))
plt.subplot(2,1,1)
for column in merged_data.columns:
    if (column == 'TOPICSETF' or column == 'diff_data') : continue
    plt.plot(merged_data.index, merged_data[column], label=column)

plt.title("Nikkei 225, Topix", fontsize=16)
#plt.xlabel("Date", fontsize=12)
#plt.ylabel("Value", fontsize=12)
plt.legend(fontsize=12)
plt.grid(True)
plt.tight_layout()

plt.subplot(2,1,2)
plt.plot(merged_data.index, merged_data['diff_data'], label=column)
plt.legend()
plt.grid(True)
plt.tight_layout()

plt.show()

# 相関係数の表示
print("Correlation Matrix:")
print(correlation_matrix)
