# -*- Coding: UTF-8 -*-
import numpy as np
from matplotlib import pyplot as plt


def CalFunc():
    # 指数関数のxを便宜上、0.1間隔で　-1 < x < 5 の範囲を指定
    xmin = -1
    xmax = 5
    xinterval = 0.1
    x = np.arange(xmin, xmax, xinterval)
    # yを算出
    y = 4**x - 2**(x+1) + 5

    return x, y


# グラフを作成する関数
def MakeGraph(x, y):

    ########## 指数関数をグラフに図示 ##########
    plt.plot(x,y)

    ########## グラフにx軸,y軸（0）を図示 ##########
    # 補助線（0）を作成　[axhline：水平　axvline:垂直]
    plt.axhline(y = 0, color = "gray")
    plt.axvline(x = 0, color = "gray")
    ############################################

    # グラフを表示
    plt.show()


# メイン処理
if __name__ == '__main__':
    # y = 4**x - 2**(x+1) + 5 の値を取得
    x, y = CalFunc()

    # 最大／最小のインデックス取得
    max_index = np.argmax(y)
    min_index = np.argmin(y)

    # 最大値／最小値を表示
    print('最大値：' + str(y[max_index]))
    print('最小値：' + str(y[min_index]))

    # y = 4**x - 2**(x+1) + 5 のグラフの作成
    MakeGraph(x, y)
