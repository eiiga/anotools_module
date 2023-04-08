# -*- Coding:UTF-8 -*-
import tkinter as tk
import tkinter.ttk as ttk
import tkinter.messagebox as msg
import numpy as np

###########################################
# 処理名    ：データ初期化処理
# 処理内容  ：Treeviewに出力した値を全て削除
###########################################
def DataInitialization():
    tree.delete(*tree.get_children())

###########################################
# 処理名    ：変換処理
###########################################
def ChangeUnit(change_list, float_bf_area):

    # 戻り値（計算処理結果配列）の宣言
    list_af_area = []

    # 変換処理用配列の値をループ処理
    for i in range(len(change_list)):
        # 0なら掛け算
        if change_list[i][0] == 0:
            list_af_area.append(round(float_bf_area * change_list[i][1], 5))
        # 1なら割り算
        elif change_list[i][0] == 1:
            list_af_area.append(round(float_bf_area / change_list[i][1], 5))

    return list_af_area

###########################################
# 処理名   :データ反映処理
# 処理内容 :入力した面積・単位を元に変換処理を行う
###########################################
def ChangeArea():
    # 入力値を変数に格納
    float_bf_area = float(str_bf_area.get())

    # 単位のインデックスを格納
    # 0:㎡, 1:a, 2:ha, 3:坪, 4:畝, 5:反, 6:町歩
    unit_bf_area = select_bf_area.current()

    # 0:㎡
    if unit_bf_area == 0:
        # ㎡以外の単位を配列に格納（Treeview表示用）
        unit_list = ["a", "ha", "坪", "畝", "反", "町歩"]

        # 変換処理用配列に値を格納（「0：掛け算、1：割り算」、「計算値」）
        change_listM2 = np.array([[0, 0.01], [0, 0.0001], [0, 0.33],
        [1, 666], [1, 999], [1, 9999]])

        # 「㎡」変換処理
        list_af_area = ChangeUnit(change_listM2, float_bf_area)

    # 1:a
    elif unit_bf_area == 1:

        # a以外の単位を配列に格納（Treeview表示用）
        unit_list = ["㎡", "ha", "坪", "畝", "反", "町歩"]

        # 変換処理用配列に値を格納（「0：掛け算、1：割り算」、「計算値」）
        change_listA = np.array([[0, 100], [1, 100], [0, 30],
        [1, 6.6], [1, 9.9], [1, 99]])

        # 「a」変換処理
        list_af_area = ChangeUnit(change_listA, float_bf_area)

    # 2:ha
    elif unit_bf_area == 2:

        # ha以外の単位を配列に格納（Treeview表示用）
        unit_list = ["㎡", "a", "坪", "畝", "反", "町歩"]

        # 変換処理用配列に値を格納（「0：掛け算、1：割り算」、「計算値」）
        change_listHa = np.array([[0, 10000], [0, 100], [0, 3000],
        [1, 16], [1, 0.1], [1, 0.01]])

        # 「ha」変換処理
        list_af_area = ChangeUnit(change_listHa, float_bf_area)

    # 3:坪
    elif unit_bf_area == 3:

        # 坪以外の単位を配列に格納（Treeview表示用）
        unit_list = ["㎡", "a", "ha", "畝", "反", "町歩"]

        # 変換処理用配列に値を格納（「0：掛け算、1：割り算」、「計算値」）
        change_listTsubo = np.array([[0, 3.3], [1, 30], [1, 3000],
        [1, 200], [1, 300], [1, 3000]])

        # 「坪」変換処理
        list_af_area = ChangeUnit(change_listTsubo, float_bf_area)

    # 4:畝
    elif unit_bf_area == 4:

        # 畝以外の単位を配列に格納（Treeview表示用）
        unit_list = ["㎡", "a", "ha", "坪", "反", "町歩"]

        # 変換処理用配列に値を格納（「0：掛け算、1：割り算」、「計算値」）
        change_listUne = np.array([[0, 666], [0, 6.6], [0, 16],
        [0, 200], [0, 0.66], [0, 0.067]])

        # 「畝」変換処理
        list_af_area = ChangeUnit(change_listUne, float_bf_area)

    # 5:反
    elif unit_bf_area == 5:

        # 反以外の単位を配列に格納（Treeview表示用）
        unit_list = ["㎡", "a", "ha", "坪", "畝", "町歩"]

        # 変換処理用配列に値を格納（「0：掛け算、1：割り算」、「計算値」）
        change_listTan = np.array([[0, 999], [0, 9.99], [0, 0.099],
        [0, 300], [0, 1.67], [0, 0.1]])

        # 「反」変換処理
        list_af_area = ChangeUnit(change_listTan, float_bf_area)

    # 6:町歩
    elif unit_bf_area == 6:

        # 町歩以外の単位を配列に格納（Treeview表示用）
        unit_list = ["㎡", "a", "ha", "坪", "畝", "反"]

        # 変換処理用配列に値を格納（「0：掛け算、1：割り算」、「計算値」）
        change_listTyobu = np.array([[0, 9999], [0, 99.99], [0, 0.99],
        [0, 3000], [0, 16.7], [0, 10]])

        # 「町歩」変換処理
        list_af_area = ChangeUnit(change_listTyobu, float_bf_area)

    # ツリーに変換結果を反映
    for i in range(len(list_af_area)):
        tree.insert("", "end", values=(list_af_area[i], unit_list[i]))


###########################################
# 処理名   :変換ボタン押下処理
# 処理内容 :
#           1.データを初期化する
#           2.面積を変換する
###########################################
def Click_Henkan_Btn():
    try:
        # データ初期化処理
        DataInitialization()
        # データ変換処理
        ChangeArea()
    except:
        msg.showinfo("エラー", "想定外のエラーが発生しました")



###########################################
# Tkinterの画面設定
###########################################
# ウィンドウの設定
base = tk.Tk()
base.title("面積変換")
canvas = tk.Canvas(base, width=300, height=300, bd=0, highlightthickness=0)
canvas.pack()

#入力値を保持
str_bf_area = tk.StringVar()

# 変換前面積ラベル
l_bf_area = tk.Label(base, text="面積", font=("",20))
l_bf_area.place(x=20, y=20)
# 変換前面積テキストボックス
txtbox_bf_area = tk.Entry(base, width=10, textvariable=str_bf_area)
txtbox_bf_area.place(x=70, y=20)

# プルダウンの設定
select_bf_area = ttk.Combobox(base, width=5, justify='center', state='readonly')
select_bf_area["values"] = ("㎡", "a", "ha", "坪", "畝", "反", "町歩")
select_bf_area.current(0)
select_bf_area.place(x=180, y=22)

# 変換ボタン関係の設定
btn_seldata = tk.Button(base, text="変換", command=Click_Henkan_Btn)
btn_seldata.place(x=140, y=50)

# Treeviewの設定
tree = ttk.Treeview(base, height=10, columns=(0, 1))
tree["show"] = "headings"
tree.column(0, width=100)
tree.column(1, width=100)
tree.heading(0, text='面積')
tree.heading(1, text='単位')
tree.place(x=50, y=75)

# ウィンドウの維持
base.mainloop()
