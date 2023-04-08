import math

import customtkinter as ctk
import tkinter.messagebox as msg

# 数字チェック処理
def InputNumChk():
    # 入力値を取得
    inputdata = str_length.get()

    # 数字以外入力されていたら1
    if not inputdata.isdigit():
        msg.showinfo("注意", "入力値は整数のみ設定してください")
        return 1
    # 0以下が入力されたら2
    if not int(inputdata) > 0:
        msg.showinfo("注意", "入力値は0より大きい値を設定してください")
        return 2
    
    return 0


# 立方体作成処理
def MakeCube():
    # 数字チェック
    chknum = InputNumChk()
    # 数字の場合（＝0）
    if chknum == 0:
        # 入力した数字をfloat型で取得
        float_length = float(str_length.get())

        # 立方体作成画面の範囲を算出
        tmp_range = int(float_length * math.sqrt(2) + float_length + 10)
        base_range = str(tmp_range) + 'x' + str(tmp_range)

        # 立方体作成画面のインスタンス
        base_cube = ctk.CTk()
        # 立方体作成画面の範囲を設定
        base_cube.geometry(base_range)

        # 立方体作成画面のタイトルセット
        base_cube.title("立方体作成画面")

        # 立方体を描くキャンバス設定
        canvas = ctk.CTkCanvas(base_cube)
        canvas.pack(fill=ctk.BOTH, expand=True)

        # 立方体描画開始のx,y座標セット
        start_x = tmp_range / 2
        start_y = 5

        # 三平方の定理：辺の長さ算出（1：√2）
        distance = float_length / math.sqrt(2)

        # 上部の「^」部分を描画
        canvas.create_line(start_x, start_y, start_x - distance, start_y + distance, width=1)
        canvas.create_line(start_x, start_y, start_x + distance, start_y + distance, width=1)

        # 中間x,y座標をセット
        start_x1 = start_x - distance
        start_x2 = start_x + distance
        start_y1 = start_y + distance

        # 上部の「V」部分を描画
        canvas.create_line(start_x1, start_y1, start_x1 + distance, start_y1 + distance, width=1)
        canvas.create_line(start_x2, start_y1, start_x2 - distance, start_y1 + distance, width=1)

        # 中間y座標をセット
        start_y2 = start_y1 + distance

        # 上部と下部をつなげる「｜」部分を描画（後ろ側は点線）
        canvas.create_line(start_x1, start_y1, start_x1, start_y1 + float_length, width=1)
        canvas.create_line(start_x2, start_y1, start_x2, start_y1 + float_length, width=1)
        canvas.create_line(start_x, start_y2, start_x, start_y2 + float_length, width=1)
        canvas.create_line(start_x, start_y, start_x, start_y + float_length, width=1, dash=(5, 3))

        # 中間y座標をセット
        start_y3 = start_y1 + float_length

        # 下部の「◇」部分を描画（後ろ側は点線）
        canvas.create_line(start_x1, start_y3, start_x, start_y2 + float_length, width=1)
        canvas.create_line(start_x2, start_y3, start_x, start_y2 + float_length, width=1)
        canvas.create_line(start_x1, start_y3, start_x, start_y + float_length, width=1, dash=(5, 3))
        canvas.create_line(start_x2, start_y3, start_x, start_y + float_length, width=1, dash=(5, 3))

        # 立方体作成画面を表示
        base_cube.mainloop()
    

# メイン処理
if __name__ == '__main__':
    # カラーテーマを設定
    ctk.set_appearance_mode("light")

    # メイン画面のインスタンス
    root = ctk.CTk()
    # メイン画面の範囲を設定
    root.geometry("300x100")

    # メイン画面のタイトル設定
    root.title("立方体作成ツール")

    # 入力値の値を保持（文字列型）
    str_length = ctk.StringVar()

    # 入力のラベルを設定
    length_label = ctk.CTkLabel(root, text="長さ：")
    length_label.place(x=45, y=20)
    # 入力用のテキストボックスを設定
    length_entry = ctk.CTkEntry(root, textvariable=str_length)
    length_entry.place(x = 85, y = 20)

    # 「作成」ボタンの設定
    make_button = ctk.CTkButton(root, text="作成", command=MakeCube)
    make_button.place(x=85, y=60)

    # メイン画面の表示
    root.mainloop()