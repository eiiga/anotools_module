# -*- Coding:UTF-8 -*-
import tkinter as tk
import tkinter.ttk as ttk
import pandas as pd

###########################################
# 処理名    ：データ初期化処理
# 処理内容  ：Treeviewに出力した値を全て削除
###########################################
def DataInitialization():
    tree.delete(*tree.get_children())

###########################################
# 処理名   :データ反映処理
# 処理内容 :csvファイルを読み込みTreeviewに反映
###########################################
def InputCsv():
    df = pd.read_csv("SpeciesData.csv")
    for i in range(len(df)):
        tree.insert("", "end", values=(df.iloc[i][0], df.iloc[i][1]))


###########################################
# 処理名   :読込ボタン押下処理
# 処理内容 :
#           1.データを初期化する
#           2.csvファイルを読み込みTreeviewに出力
###########################################
def FncInput():
    # データ初期化処理
    DataInitialization()
    # データ反映処理
    InputCsv()


###########################################
# Tkinterの画面設定
###########################################
# ウィンドウの設定
base = tk.Tk()
base.title("CSV読込")
canvas = tk.Canvas(base, width=300, height=300, bd=0, highlightthickness=0)
canvas.pack()

#読込ボタン関係の設定
btn_inputcsv = tk.Button(base, text="読込", command=FncInput)
btn_inputcsv.place(x=130, y=20)

# Treeviewの設定
tree = ttk.Treeview(base, columns=(0, 1))
tree["show"] = "headings"
tree.column(0, width=100)
tree.column(1, width=100)
tree.heading(0, text='品種')
tree.heading(1, text='重さ(g)')
tree.place(x=50, y=50)

# ウィンドウの維持
base.mainloop()
