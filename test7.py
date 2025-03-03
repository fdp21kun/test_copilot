import pandas as pd
import yfinance as yf
from tqdm import tqdm
from pathlib import Path

"""
  Yfinanceを使用して、株価データを取得するサンプルコードです。

  Yfinanceでは、1つのアプリケーションID（Client ID）に対して、1分で300回を超えると
  利用回数に制限がかかります。制限がかかっている場合は、
  429 Too Many Requestsのエラーレスポンスが返却されます。
"""

# 東証上場銘柄一覧の読み込み
# 日本取引所グループ（JPX）の公式サイトからダウンロードしたExcelファイルを指定
file_path = "data_j.xls"  # JPXからダウンロードしたファイル名
df = pd.read_excel(file_path)

# ETFおよび内国株式に絞り込み
df_filtered = df[df['市場・商品区分'].str.contains('内国株式|ETF')]

# データ取得期間の設定
start_date = "2022-01-01"
end_date = "2025-02-01"

# 各銘柄のデータを取得
for code, name in tqdm(zip(df_filtered['コード'], df_filtered['銘柄名']), total=len(df_filtered)):
    if (code > 10000):   # 特殊株式なのでスキップ
        continue
    ticker = f"{code}.T"  # yfinance用ティッカー形式
    try:
        file_path = Path(f"stockData/{code}_{name}.csv")
        if (file_path.exists()):
            print(f"データ取得済み: {ticker}")
            continue
        # 株価データを取得
        stock_data = yf.download(ticker, start=start_date, end=end_date)
        if not stock_data.empty:
            # CSVとして保存（銘柄コードと銘柄名を使用）
            relative_path = file_path.relative_to(Path.cwd())
            stock_data.to_csv(relative_path)
    except Exception as e:
        print(f"データ取得エラー: {ticker} - {e}")
