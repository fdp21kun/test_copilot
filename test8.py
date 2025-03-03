import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 銘柄の設定（例: トヨタ自動車とホンダ）
ticker1 = "7203.T"  # トヨタ自動車
ticker2 = "7267.T"  # ホンダ

# データ取得期間
start_date = "2022-01-01"
end_date = "2025-01-01"

# 表示オプションを変更
pd.set_option('display.max_rows', None)  # 全行を表示
pd.set_option('display.max_columns', None)  # 全列を表示

# データ取得
data1 = yf.download(ticker1, start=start_date, end=end_date, multi_level_index=None)['Close']
data2 = yf.download(ticker2, start=start_date, end=end_date, multi_level_index=None)['Close']

# データフレームの作成
data = pd.DataFrame({
    ticker1: data1,
    ticker2: data2
}).dropna()

# スプレッドの計算（価格比率の対数を取る）
data['Spread'] = np.log(data[ticker1] / data[ticker2])

# 

data['Spread_Z'] = (data['Spread'] - data['Spread'].mean()) / data['Spread'].std()

# トレードルールの設定（スプレッドが±2シグマを超えた場合にエントリー）
entry_threshold = 2
exit_threshold = 0

data['Position'] = 0  # トレードポジション
data.loc[data['Spread_Z'] > entry_threshold, 'Position'] = -1  # 売り
data.loc[data['Spread_Z'] < -entry_threshold, 'Position'] = 1  # 買い

# ポジションのシフト（スプレッド収束時にエグジット）
data['Position'] = data['Position'].shift(1).fillna(0)
data.loc[data['Spread_Z'].abs() < exit_threshold, 'Position'] = 0

# トレードパフォーマンスの計算
data['Returns'] = data['Position'] * (data['Spread'].diff())  # スプレッド変化での収益
cumulative_returns = data['Returns'].cumsum()

# グラフ描画
plt.figure(figsize=(12, 6))
plt.plot(data.index, cumulative_returns, label='Cumulative Returns')
plt.title("Pair Trading Performance", fontsize=16)
plt.xlabel("Date", fontsize=12)
plt.ylabel("Cumulative Returns", fontsize=12)
plt.legend(fontsize=12)
plt.grid(True)
plt.tight_layout()
plt.show()
