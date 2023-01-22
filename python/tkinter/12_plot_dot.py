import tkinter as tk

# 円を移動する処理
def Click_Btn(direction):
    # 現在の円のx軸・y軸（from to）の位置を取得
    global oval_x1
    global oval_y1
    global oval_x2
    global oval_y2

    # 円のオブジェクトを取得
    global oval

    # 円を削除
    canvas.delete(oval)

    # 「▶︎」ボタン押下時の場合
    if direction == "right":
        # x軸の最大より小さい場合
        if oval_x1 < 260:
            # 円のx軸をインクリメント
            oval_x1 = oval_x1 + 40
            oval_x2 = oval_x2 + 40
    # 「◀︎」ボタン押下時の場合
    elif direction == "left":
        # x軸の最小より大きい場合
        if oval_x1 > 30:
            # 円のx軸をデクリメント
            oval_x1 = oval_x1 - 40
            oval_x2 = oval_x2 - 40
    # 「▲」ボタン押下時の場合
    elif direction == "up":
        # y軸の最小より大きい場合
        if oval_y1 > 30:
            # 円のy軸をデクリメント
            oval_y1 = oval_y1 - 40
            oval_y2 = oval_y2 - 40
    # 「▼」ボタン押下時の場合
    elif direction == "down":
        # y軸の最大より小さい場合
        if oval_y1 < 260:
            # 円のy軸をインクリメント
            oval_y1 = oval_y1 + 40
            oval_y2 = oval_y2 + 40
    
    # 円を描画
    oval = canvas.create_oval(oval_x1, oval_y1, oval_x2, oval_y2, width=1, fill="blue")


### メイン処理 ###

# 画面のインスタンス
base = tk.Tk()
# 画面のタイトル設定
base.title("plot dot")
# 画面のサイズ設定
base.geometry("300x350")

# 罫線や円を描画するための前設定
canvas = tk.Canvas(base, bg="white")
canvas.pack(fill=tk.BOTH, expand=True)

# 罫線用x軸y軸の開始初期値をセット
x = 30
y = 30

# 7回繰り返し
for _ in range(7):
    # y軸方向に罫線を引く
    canvas.create_line(x, 30, x, 270, width=1)
    # x軸のインクリメント
    x = x + 40

# 7回繰り返し
for _ in range(7):
    # x軸方向に罫線を引く
    canvas.create_line(30, y, 270, y, width=1)
    # y軸のインクリメント
    y = y + 40

# 円のx軸・y軸（from to）位置の初期値をセット
oval_x1 = 140
oval_y1 = 140
oval_x2 = 160
oval_y2 = 160

# 初期の円を描画
oval = canvas.create_oval(oval_x1, oval_y1, oval_x2, oval_y2, width=1, fill="blue")

# 「▶︎」ボタンの設定
btn_right = tk.Button(base, text="▶︎", command=lambda: Click_Btn("right"))
btn_right.place(x=160, y=300)

# 「◀︎」ボタンの設定
btn_left = tk.Button(base, text="◀︎", command=lambda: Click_Btn("left"))
btn_left.place(x=120, y=300)

# 「▲」ボタンの設定
btn_up = tk.Button(base, text="▲", command=lambda: Click_Btn("up"))
btn_up.place(x=140, y=280)

# 「▼」ボタンの設定
btn_down = tk.Button(base, text="▼", command=lambda: Click_Btn("down"))
btn_down.place(x=140, y=320)

# 画面の表示
base.mainloop()