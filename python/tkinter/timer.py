# -*- Coding: UTF-8 -*-
import tkinter as tk
import tkinter.messagebox as msg
import time

# 整数判定
def is_integer(n):
    try:
        return int(n)
    except ValueError:
        return False

# タイマー起動関数
def StartTimer():
    print('#####StartTimer処理開始#####')
    # 入力値を変数に格納
    Str_input_num = Str_input.get()
    # 整数判定
    int_input_num = is_integer(Str_input_num)
    if int_input_num == False:
        msg.showinfo("入力結果", "入力値が不適切です。")
    else:
        # 1から60分までチェック
        if int_input_num >= 1 and int_input_num <= 60:
            # ラベルに貼り付け
            label_count["text"] = "あと " + str(int_input_num) + "分"
            # 入力値回数分ループ処理
            for i in range(int_input_num):
                # ラベルに貼り付け
                label_count["text"] = "あと " + str(int_input_num - i) + "分"
                print("あと " + str(int_input_num - i) + "分")
                # 1分（60秒）待機
                time.sleep(60)
            label_count["text"] = "あと 0 分"
            # 終了メッセージ
            msg.showinfo("終了", str(int_input_num) + "分経ちました！！")
        else:
            msg.showinfo("入力結果", "1から60分で入力してください。")




##############
# 画面の設定
##############
base = tk.Tk()

# 画面のタイトルを設定
base.title("タイマー")


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
btn_input = tk.Button(base, text="スタート", command=StartTimer)
# ボタンの配置場所
btn_input.place(x=350, y=105)

# ラベルの作成
label_count = tk.Label(base, text="あと 0 分")
label_count.place(x=200, y=170)

# 画面の表示
base.mainloop()
