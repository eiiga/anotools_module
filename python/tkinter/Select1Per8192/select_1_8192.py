import random

import tkinter as tk
import tkinter.ttk as ttk


# 1/2判定処理
def check_answer():
    # 0, 1か乱数を取得
    ans_int = random.randint(0, 1)

    # 正解：乱数と選択したラジオボタン判定
    if ans_int == radiobtn_value.get():

        # 初回正解判定
        if result_Count.get() == 0:
            # 確率分母に2をセット
            result_Denominator.set(2)

        else:
            # 確率分母を2倍
            result_Denominator.set(result_Denominator.get() * 2 )
            
        # 正解回数インクリメント
        result_Count.set(result_Count.get() + 1)

    # 不正解
    else:
        # 正解数と確率分母を初期化
        result_Count.set(0)
        result_Denominator.set(0)
    
    if len(list_ans_top_10) > 10:
        list_ans_top_10.pop(0)

    if ans_int == 0:
        list_ans_top_10.append('左')
    else:
        list_ans_top_10.append('          右')

    # ラベルの文字を更新
    label_result["text"] = str(result_Count.get()) + "回正解：1/" + str(result_Denominator.get())
    
    ans_top_10 = ''
    
    for ans in list_ans_top_10:
        ans_top_10 = ans_top_10 + ans + '\n'
    
    label_ans_list["text"] = ans_top_10


# メイン処理
if __name__ == '__main__':

    # tkinterのインスタンス
    base = tk.Tk()
    # タイトル設定
    base.title("1/8192")
    # 画面幅の設定
    base.geometry("500x300")

    # ラジオボタンの値を保持
    radiobtn_value = tk.IntVar()

    # ラベルの値を保持
    result_Count = tk.IntVar()
    result_Denominator = tk.IntVar()
    
    # 回答一覧リスト
    list_ans_top_10 = []

    # 初期値：正解数と確率分母の数
    result_Count.set(0)
    result_Denominator.set(0)

    # ラジオボタン：左
    radiobtn_right_left = ttk.Radiobutton(
        base,
        text='左',
        value=0,
        variable=radiobtn_value)
    radiobtn_right_left.place(x=100, y=100)

    # ラジオボタン：右
    radiobtn_right_left = ttk.Radiobutton(
        base,
        text='右',
        value=1,
        variable=radiobtn_value)
    radiobtn_right_left.place(x=300, y=100)

    # 正解数と確率ラベルをセット
    label_result = tk.Label(base)
    label_result.place(x=180, y=40) 
    label_result["text"] = str(result_Count.get()) + "回正解：1/" + str(result_Denominator.get())

   # 回答ラベルセット
    label_ans = tk.Label(base)
    label_ans.place(x=400, y=40) 
    label_ans["text"] = "直近の正解"
    
    # 回答一覧ラベルセット
    label_ans_list = tk.Label(base)
    label_ans_list.place(x=400, y=80) 
    label_ans_list["text"] = ""

    # 回答ボタンの設定
    btn_answer = tk.Button(base, text="回答", command=check_answer)
    btn_answer.place(x=200, y=200)

    # 画面の表示
    base.mainloop()