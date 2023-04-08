# -*- Coding:UTF-8 -*-
import qrcode as qr
import tkinter as tk
from PIL import ImageTk

###########################################
# QRコード作成関数
###########################################
def MakeQrCode():
    qr_label.qr_img = qr.make(encode_text.get())
    img_width, img_height = qr_label.qr_img.size
    qr_label.tk_img = ImageTk.PhotoImage(qr_label.qr_img)
    qr_label.config(image=qr_label.tk_img, width=img_width, height=img_height)
    qr_label.pack()


###########################################
# Tkinterの画面設定
###########################################
base = tk.Tk()
base.title('QRコード作成')

# QRコードにする文字列を保持する変数
encode_text = tk.StringVar()

# 入力フォーム
input_area = tk.Frame(base, relief=tk.RAISED, bd=2)
input_area.pack(pady=5)
entry = tk.Entry(input_area, textvariable=encode_text).pack(side=tk.LEFT)

# ボタンの作成
btn_encode = tk.Button(input_area, text='QRコード作成', command=MakeQrCode)
btn_encode.pack(side=tk.LEFT)

# QRコード表示フォーム
image_area = tk.Frame(base, relief=tk.SUNKEN, bd=2)
image_area.pack(padx=3, pady=1)
qr_label = tk.Label(image_area)

# 画面の表示
base.mainloop()
