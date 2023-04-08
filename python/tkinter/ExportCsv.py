# -*- Coding:UTF-8 -*-
import tkinter as tk
import tkinter.messagebox as msg
import pandas as pd


# CSV出力処理
def ExportCsvFile():
    # 入力値を変数に格納
    species_data = str_species.get()
    weight_data = str_weight.get()
    # 入力フォームの値がない場合は、CSV出力処理しない
    if species_data == '' or weight_data == '':
        msg.showinfo("お知らせ", "データが入力されていません")
    else:
        df = pd.DataFrame({'Species':[species_data], 'Weight(g)':[weight_data]})
        df.to_csv("SpeciesData.csv", mode='a', header=False, index=False)
        msg.showinfo("お知らせ", "CSV出力が完了しました")


###########################################
# Tkinterの画面設定
###########################################
# ウィンドウの設定
base = tk.Tk()
base.title("CSV出力")
canvas = tk.Canvas(base, width=300, height=150, bd=0, highlightthickness=0)
canvas.pack()

#入力値を保持
str_species = tk.StringVar()
str_weight = tk.StringVar()

# 種類ラベルフォーム
l_species = tk.Label(base, text="種別：")
l_species.place(x=50, y=25)

# 種類入力テキストフォーム
txtbox_species = tk.Entry(base, width=10, textvariable=str_species)
txtbox_species.place(x=100, y=20)


# 重さラベルフォーム
l_species = tk.Label(base, text="重さ：")
l_species.place(x=50, y=65)

# 重さ入力テキストフォーム
txtbox_weight = tk.Entry(base, width=10, textvariable=str_weight)
txtbox_weight.place(x=100, y=60)

# CSV出力ボタン関係の設定
btn_seldata = tk.Button(base, text="CSV出力", command=ExportCsvFile)
btn_seldata.place(x=100, y=100)

# ウィンドウの維持
base.mainloop()
