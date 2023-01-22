# -*- Coding: UTF-8 -*-
import tkinter as tk

# カウントダウン
def CountDown():
    # 値を減少させる
    decrease_num = count_num.get()
    decrease_num = decrease_num - 1
    count_num.set(decrease_num)

    # ラベルに貼り付け
    label_count["text"] = count_num.get()


# リセット
def CountReset():
    # 値を0に戻す
    reset_num = 0
    count_num.set(reset_num)

    # ラベルに貼り付け
    label_count["text"] = count_num.get()


# カウントアップ
def CountUp():
    # 値を増加させる
    increase_num = count_num.get()
    increase_num = increase_num + 1
    count_num.set(increase_num)

    # ラベルに貼り付け
    label_count["text"] = count_num.get()


##############
# 画面の設定
##############
base = tk.Tk()
# 画面のタイトルを設定
base.title("カウンター")
# 画面のサイズを設定する
#    width   ：幅(px)
#    height  ：高さ(px)
canvas = tk.Canvas(base, width=250, height=250)
canvas.pack()

# カウント初期値をセット
count_num = tk.IntVar()
count_num.set(0)

# 表示用のラベル
label_count = tk.Label(anchor='center')
label_count.place(x=120, y=80)
label_count["text"] = count_num.get()

# カウントダウンボタンの作成と配置場所
btn_count_down = tk.Button(base, text="-", command=CountDown)
btn_count_down.place(x=50, y=155)

# リセットボタンの作成と配置場所
btn_count_reset = tk.Button(base, text="リセット", command=CountReset)
btn_count_reset.place(x=100, y=155)

# カウントアップボタンの作成と配置場所
btn_count_reset = tk.Button(base, text="＋", command=CountUp)
btn_count_reset.place(x=200, y=155)


# 画面の表示
base.mainloop()
