# -*- Coding: UTF-8 -*-
import tkinter as tk
import tkinter.messagebox as msg

# 入力値チェック関数
def InputNumChk():
    # チェックデータ格納
    inputdata = []
    inputdata.append(str_sanpuryo.get())
    inputdata.append(str_kishaku.get())

    # 配列に格納したデータ分だけループ処理
    for i in range(len(inputdata)):
        # 数字以外入力されていたら1
        if not inputdata[i].isdigit():
            return 1
        # 0以下が入力されたら2
        if not int(inputdata[i]) > 0:
            return 2



    return 0

# 計算ボタン押下時の処理（濃度計算）
def Click_CalCon():
    # 数字チェック
    chknum = InputNumChk()
    if chknum == 1:
        msg.showinfo("注意", "入力値は数字のみ設定してください")

    elif chknum == 2:
        msg.showinfo("注意", "入力値は0より大きい値を設定してください")

    elif chknum == 0:
        # 入力値を取得（散布量はmlに変換）
        int_sanpuryo_ml = int(str_sanpuryo.get()) * 1000
        int_kishaku = int(str_kishaku.get())

        # 濃度計算
        calcon = int_sanpuryo_ml / int_kishaku

        msg.showinfo("計算結果", "農薬を" + str(round(calcon, 2)) + "g(mL)用意して下さい")

    else:
        msg.showinfo("エラー", "想定外のエラーが発生しました")


###########################################
# トップ画面の設定
###########################################
# ウィンドウの設定
base = tk.Tk()
base.title("濃度計算")
canvas = tk.Canvas(base, width=400, height=150, bd=0, highlightthickness=0)
canvas.pack()

#入力値を保持
str_sanpuryo = tk.StringVar()
str_kishaku = tk.StringVar()

# 散布量ラベル
l_sanpuryo = tk.Label(base, text="散布量（L）", font=("",20))
l_sanpuryo.place(x=40, y=20)
# 散布量テキストボックス
txtbox_sanpuryo = tk.Entry(base, width=10, textvariable=str_sanpuryo)
txtbox_sanpuryo.place(x=200, y=20)

# 希釈倍率ラベル
l_kishaku = tk.Label(base, text="希釈倍率（倍）", font=("",20))
l_kishaku.place(x=40, y=50)
# 希釈倍率テキストボックス
txtbox_kishaku = tk.Entry(base, width=10, textvariable=str_kishaku)
txtbox_kishaku.place(x=200, y=50)

# 計算ボタン関係の設定
btn_seldata = tk.Button(base, text="計算", command=Click_CalCon)
btn_seldata.place(x=150, y=100)

# 画面表示
base.mainloop()
