# -*- Coding: UTF-8 -*-
import tkinter as tk
import tkinter.messagebox as msg

# メッセージボックスを表示する関数
#   処理：画面で入力した値をメッセージボックスに表示
def OpenMessageBox():
    msg.showinfo("入力結果", Str_input.get())


##############
# 画面の設定
##############
base = tk.Tk()

# 画面のタイトルを設定
base.title("テキスト入力画面")


# 画面のサイズを設定する
#    width   ：幅(px)
#    height  ：高さ(px)
canvas = tk.Canvas(base, width=500, height=250)
canvas.pack()

# 入力値を変数に格納
Str_input = tk.StringVar()

# 入力フォーム（テキストボックス）
tx_input = tk.Entry(base, textvariable=Str_input)
# テキストボックスの配置場所
tx_input.place(x=150, y=100)

# ボタンの作成
btn_input = tk.Button(base, text="送信", command=OpenMessageBox)
# ボタンの配置場所
btn_input.place(x=350, y=105)

# 画面の表示
base.mainloop()
