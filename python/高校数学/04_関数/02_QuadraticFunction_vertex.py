# -*- Coding: UTF-8 -*-
import numpy as np
from matplotlib import pyplot as plt

# 2次関数の頂点座標を算出する関数
# 引数     ： y = ax**2 + bx + c の[a, b, c]
# 戻り値   ：頂点(p, q)
def CheckVertex(a:int, b:int, c:int) -> list:
    # 変数宣言（戻り値用の配列）
    result_data = []

    # 頂点(p, q)の[p]を算出
    p = -1 * (b / (2 * a))

    # [p]を配列にセット
    result_data.append(p)

    # 頂点(p, q)の[q]を算出
    q = -1 * ((b ** 2) - (4 * a * c)) / (4 * a)

    # [p]を配列にセット
    result_data.append(q)

    return result_data

# グラフを作成する関数
# 引数   ：配列[傾き, 切片]
def MakeGraph(a:int, b:int, c:int, data: list):
    # 頂点座標を変数にセット
    p = data[0]
    q = data[1]

    ########## 2次関数をグラフに図示 ##########
    # 2次関数のxを便宜上、0.1間隔で　-1 < x < 5 の範囲を指定
    xmin = -1
    xmax = 5
    xinterval = 0.1
    x = np.arange(xmin, xmax, xinterval)

    # yを算出
    y = (a * (x ** 2)) + (b * x) + c

    # グラフを作成
    plt.plot(x,y)
    ########################################

    ########## グラフにx軸,y軸から頂点までを点線で図示 ##########
    # 補助線を点線で作成　[hlines：水平　vlines:垂直]
    plt.hlines([q], 0, p, "gray", linestyles='dashed')
    plt.vlines([p], 0, q, "gray", linestyles='dashed')
    #######################################################

    ########## グラフにx軸,y軸（0）を図示 ##########
    # 補助線（0）を作成　[axhline：水平　axvline:垂直]
    plt.axhline(y = 0, color = "gray")
    plt.axvline(x = 0, color = "gray")
    ############################################

    # グラフを表示
    plt.show()


# メイン処理
if __name__ == '__main__':
    # (1) y = 3x**2 - 12x + 15の頂点座標(p,q)を算出
    a = 3
    b = -12
    c = 15

    # 2次関数の頂点座標を算出する
    data = CheckVertex(a, b, c)

    print('頂点座標(' + str(data[0]) + ',' + str(data[1]) + ')')

    # グラフの作成
    MakeGraph(a, b, c, data)

    # (2) y = -2x**2 + 8x - 16の頂点座標(p,q)を算出
    a = -2
    b = 8
    c = -16

    # 2次関数の頂点座標を算出する
    data = CheckVertex(a, b, c)

    print('頂点座標(' + str(data[0]) + ',' + str(data[1]) + ')')

    # グラフの作成
    MakeGraph(a, b, c, data)
