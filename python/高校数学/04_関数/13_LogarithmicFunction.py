# -*- Coding:UTF-8 -*-
import numpy as np
import math
from matplotlib import pyplot as plt


# グラフを作成する関数
def MakeGraph(a: int) -> None:
    ########## 対数関数をグラフに図示 ##########
    # 対数関数のxを便宜上、0.1間隔で　0.1 < x < 3 の範囲を指定
    xmin = 0.1
    xmax = 3
    xinterval = 0.1
    x = np.arange(xmin, xmax, xinterval)

    y = []
    # yを算出
    for i in range(len(x)):
        y.append(math.log(x[i], a))

    # グラフを作成
    plt.plot(x, y)
    ########################################

    ########## グラフにx軸,y軸（0）を図示 ##########
    # 補助線（0）を作成　[axhline：水平　axvline:垂直]
    plt.axhline(y=0, color="gray")
    plt.axvline(x=0, color="gray")
    ############################################

    # グラフを表示
    plt.show()


if __name__ == '__main__':
    # y = log(3)x のグラフ作成
    a = 3
    MakeGraph(a)

    # y = log(1/2)x のグラフ作成
    a = 1 / 2
    MakeGraph(a)
