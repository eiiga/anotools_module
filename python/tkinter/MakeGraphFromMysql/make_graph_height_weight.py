from matplotlib import pyplot as plt
import pandas as pd
import seaborn as sns
import tkinter as tk

from connect_mysql import ConnectMysql, SelectUserHeightWeght


def FncInput():
    sql_connect = ConnectMysql()
    connect_info = sql_connect.connector_mysql()

    select_user = SelectUserHeightWeght()
    result_data = select_user.select_user_height_weight(connect_info)
    df = pd.DataFrame(result_data)
    sns.set()
    sns.jointplot(x="height", y="weight", data=df, color='black')
    plt.show()


# main処理
if __name__ == '__main__':
    # ウィンドウの設定
    base = tk.Tk()
    base.title("散布図作成")
    canvas = tk.Canvas(base, width=150, height=50, bd=0, highlightthickness=0)
    canvas.pack()

    # 読込ボタン関係の設定
    btn_inputcsv = tk.Button(base, text="散布図作成", command=FncInput)
    btn_inputcsv.place(x=35, y=15)

    base.mainloop()


# 参考URL
# https://python.keicode.com/advanced/tkinter-widget-radiobutton.php
