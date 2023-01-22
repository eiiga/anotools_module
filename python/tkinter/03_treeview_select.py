# -*- Coding:UTF-8 -*-
import tkinter as tk
import tkinter.ttk as ttk
import tkinter.messagebox as msg
import pandas as pd

###########################################
# 処理名    ：データ初期化処理
# 処理内容  ：Treeviewに出力した値を全て削除
###########################################
def DataInitialization():
    tree.delete(*tree.get_children())

###########################################
# 処理名   :データ反映処理
# 処理内容 :
#       csvファイルを読み込みTreeviewに反映
#       1.入力値なし：全件検索
#       2.入力値あり：入力値を元に検索
###########################################
def SelectData():
    # 入力値を変数に格納
    selword = str_seldata.get()

    # csvファイルの読み込み
    df = pd.read_csv("SpeciesData.csv")

    # 入力値が空なら全件検索
    if selword == '':
        for i in range(len(df)):
            tree.insert("", "end", values=(df.iloc[i][0], df.iloc[i][1]))
    else:
        # 検索処理
        df_sel = df[df['Species'] == selword]

        # 検索結果数が0件ならばメッセージを出力
        if len(df_sel) == 0:
            msg.showinfo("検索結果", "データがありません")
        # 有件ならばtreeviewに出力
        else:
            for i in range(len(df_sel)):
                tree.insert("", "end", values=(df_sel.iloc[i][0], df_sel.iloc[i][1]))


###########################################
# 処理名   :検索ボタン押下処理
# 処理内容 :
#           1.データを初期化する
#           2.csvファイルを読み込みTreeviewに出力
###########################################
def FncInput():
    # データ初期化処理
    DataInitialization()
    # データ検索処理
    SelectData()


###########################################
# Tkinterの画面設定
###########################################
# ウィンドウの設定
base = tk.Tk()
base.title("CSV読込")
canvas = tk.Canvas(base, width=300, height=300, bd=0, highlightthickness=0)
canvas.pack()

#入力値を保持
str_seldata = tk.StringVar()

# 検索用テキストフォーム
txtbox_seldata = tk.Entry(base, width=10, textvariable=str_seldata)
txtbox_seldata.place(x=70, y=20)

# 検索ボタン関係の設定
btn_seldata = tk.Button(base, text="検索", command=FncInput)
btn_seldata.place(x=180, y=25)

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
