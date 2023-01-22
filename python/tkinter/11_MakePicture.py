# -*- Coding:UTF-8 -*-
import tkinter as tk
import tkinter.filedialog as fd


# 入力した値をラベルに表示する処理
def MakeLabel():
    image_label["text"] = encode_text.get()
    image_label.pack()


# ラベルを画像ファイルに保存する処理
def LabelImgSave():
    save_file_data = fd.asksaveasfilename(
        title='名前をつけて保存', initialfile='label.png')
    if save_file_data and hasattr(image_label, 'label_img'):
        image_label.save(save_file_data)


# 終了処理
def Exit():
    base.destroy()


###########################################
# Tkinterの画面設定
###########################################
base = tk.Tk()
base.title('画像メモ作成')

# 入力した文字列を保持する変数
encode_text = tk.StringVar()

# 入力フォーム
input_area = tk.Frame(base, relief=tk.RAISED, bd=2)
input_area.pack(pady=5)
entry = tk.Entry(input_area, textvariable=encode_text).pack(side=tk.LEFT)

# ボタンの作成
btn_encode = tk.Button(input_area, text='ラベルに貼り付け', command=MakeLabel)
btn_encode.pack(side=tk.LEFT)

# 入力した値の表示フォーム
image_area = tk.Frame(base, relief=tk.SUNKEN, bd=2)
image_area.pack(padx=3, pady=1)
image_label = tk.Label(image_area)

# メニューバーの設定
menu_bar = tk.Menu(base)
file_menu = tk.Menu(menu_bar)

menu_bar.add_cascade(label='file', menu=file_menu)
file_menu.add_command(label='save', command=LabelImgSave)
file_menu.add_separator()
file_menu.add_command(label='exit', command=Exit)
base.config(menu=menu_bar)

# 画面の表示
base.mainloop()
