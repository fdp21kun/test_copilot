import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# サンプルデータの作成
np.random.seed(0)
date_range = pd.date_range(start="2022-01-01", periods=100, freq='D')
data1 = np.cumsum(np.random.randn(100))  # ランダムな時系列データ1
data2 = np.cumsum(np.random.randn(100))  # ランダムな時系列データ2

# データフレームの作成
df = pd.DataFrame({'Date': date_range, 'Series1': data1, 'Series2': data2})
df.set_index('Date', inplace=True)

# 動的オフセット値の計算（平均値の差）
dynamic_offset = df['Series1'].mean() - df['Series2'].mean()
df['Series2_offset'] = df['Series2'] + dynamic_offset

# グラフ描画
plt.figure(figsize=(12, 6))

# 元のデータのプロット
plt.plot(df.index, df['Series1'], label='Series1', color='blue')
plt.plot(df.index, df['Series2'], label='Series2 (Original)', color='red')

# 動的オフセットデータのプロット
plt.plot(df.index, df['Series2_offset'], label=f'Series2 (Offset by {dynamic_offset:.2f})', color='green', linestyle='--')

# グラフの装飾
plt.title("Time Series with Dynamic Offset", fontsize=16)
plt.xlabel("Date", fontsize=12)
plt.ylabel("Value", fontsize=12)
plt.legend(fontsize=12)
plt.grid(True)
plt.tight_layout()

# グラフの表示
plt.show()
