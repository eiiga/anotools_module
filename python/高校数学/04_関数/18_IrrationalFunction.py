# -*- Coding:UTF-8 -*-
import numpy as np
import math
from matplotlib import pyplot as plt


def MakeGraph(a:int, p:int, q:int) -> None:
    ########## グラフにx軸,y軸（0）を図示 ##########
    # 補助線（0）を作成　[axhline：水平　axvline:垂直]
    plt.axhline(y = 0, color = "gray")
    plt.axvline(x = 0, color = "gray")
    ############################################

    ########## 無理関数をグラフに図示 ##########

    # xの値を0.01の間隔で設定するための変数
    xinterval = 0.01

    # aが0より大きい場合のxの範囲を指定
    if a > 0:
        xmin = p
        xmax = p + 5
        x = np.arange(xmin, xmax, xinterval)
    # aが0より小さい場合のxの範囲を指定
    elif a < 0:
        xmin = p - 5
        xmax = p + 0.01
        x = np.arange(xmin, xmax, xinterval)

    y =[]

    # yを算出
    for i in range(len(x)):
        y.append(math.sqrt(a * (x[i] - p)) + q)

    # グラフを作成
    plt.plot(x,y,color = "blue")

    ########################################


    # グラフを表示
    plt.show()


# メイン処理
if __name__ == '__main__':
    # 問題1：y = √(x - 1) + 2
    a = 1
    p = 1
    q = 2
    MakeGraph(a, p, q)

    # 問題2：y = √-1(x - 1) + 2
    a = -1
    p = 1
    q = 2
    MakeGraph(a, p, q)
