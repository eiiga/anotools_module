# -*- Coding:UTF-8 -*-
import numpy as np
import math
from matplotlib import pyplot as plt


def MakeGraph() -> None:
    # グラフにx軸,y軸（0）を図示
    # 補助線（0）を作成　[axhline：水平　axvline:垂直]
    plt.axhline(y = 0, color = "gray")
    plt.axvline(x = 0, color = "gray")

    # xの値を0.01の間隔で設定するための変数
    xinterval = 0.01
    xmin = -10
    xmax = 10
    x1 = np.arange(xmin, xmax, xinterval)

    # 問題：y = 2x + 6 について yの値を求める
    y1 = 2 * x1 + 6

    # グラフを作成
    plt.plot(x1,y1,color = "blue")

    # 逆関数をグラフに図示（xとyの値を入れ替えるだけ）
    plt.plot(y1,x1,color = "red")

    # y = xを点線で図示する。
    x = np.arange(np.min(y1), np.max(y1), xinterval)
    y = x
    plt.plot(x,y,color = "gray", linestyle='dashed')


    # グラフを表示
    plt.show()


# メイン処理
if __name__ == '__main__':

    MakeGraph()
