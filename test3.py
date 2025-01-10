"""
トヨタをソフトバンクの直近１００日分の株価を取得する
market speed2のRSSを使用
"""

import win32com.client
import time

#株式コードをListに登録(トヨタ[7203] ソフトバンク[9434])
kabu_code_list = [7203, 9434]

#作成したExcelファイルのpath
excel_file_path = r"C:\Users\kun\OneDrive\Desktop\sample.xlsx"

#Excelでの操作

#Excelオブジェクト生成
excel = win32com.client.Dispatch('Excel.Application')
#MarketSpeed2_RSS addin
addin_path = r"C:\Users\kun\AppData\Local\MarketSpeed2\Bin\rss\MarketSpeed2_RSS_64bit.xll"
excel.RegisterXLL(addin_path)

#Excelの処理を表示をさせる
excel.Visible = True

#Excelファイルを開く
wb = excel.workbooks.Open(Filename=excel_file_path)

#特定のシートを読み込む
excelSheet = wb.worksheets('Sheet1')
for code in kabu_code_list:
    
    #LoopでA1セルに株式コードを入力
    excelSheet.Range("A1").value = code
    time.sleep(2)

    #特定セルの指定
    excelCell = excelSheet.Range("D4:J104")

    #セルの値取得
    print(excelCell.value) 
    
    # >>> (('日付', '時刻', '始値', '高値', '安値', '終値', '出来高'), 
    #      ('2021/03/12', '', 8070.0, 8145.0, 8018.0, 8145.0, 6505000.0), ...

#Excelファイルを保存
wb.Save()

#Excelを閉じる
