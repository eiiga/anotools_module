# -*- Coding: UTF-8 -*-
import numpy as np
from matplotlib import pyplot as plt

# x軸との2交点と任意の1点から2次関数を決定する関数
# y = a(x - α)(x - β) を使用
# 引数     ： x軸との2交点A(x1, 0)、B(x2, 0)の[x1, x2]
#            任意の1点(x3, y3)
# 戻り値   ：y = a(x - α)(x - β) の [a]
def DecisionQuadraticFunc(x1:int, x2:int, x3:int, y3:int) -> int:
    # aの値を算出
    a = y3 / ((x3 - x1) * (x3 - x2))

    return a

# グラフを作成する関数
def MakeGraph(a:int, x1:int, x2:int, x3:int, y3:int) -> None:

    ########## 2次関数をグラフに図示 ##########
    # 2次関数のxを便宜上、0.1間隔で　-3 < x < 4 の範囲を指定
    xmin = -3
    xmax = 4
    xinterval = 0.1
    x = np.arange(xmin, xmax, xinterval)

    # yを算出
    y = a * (x - x1) * (x - x2)

    # グラフを作成
    plt.plot(x,y)
    ########################################

    ########## グラフにx軸,y軸から点Cまでを点線で図示 ##########
    # 補助線を点線で作成　[hlines：水平　vlines:垂直]
    plt.hlines([y3], 0, x3, "gray", linestyles='dashed')
    plt.vlines([x3], 0, y3, "gray", linestyles='dashed')
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
    # A(-1, 0), B(2, 0), C(3, -4)
    x1 = -1
    x2 = 2
    x3 = 3
    y3 = -4


    # x軸との2交点と任意の1点から二次関数を求める
    a = DecisionQuadraticFunc(x1, x2, x3, y3)


    print('二次関数：y = ' + str(a) + '( x - ( ' + str(x1) + ' ))( x - ( ' + str(x2) + ' ))')

    # グラフの作成
    MakeGraph(a, x1, x2, x3, y3)
