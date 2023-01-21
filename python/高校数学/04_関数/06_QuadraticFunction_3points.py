# -*- Coding:UTF-8 -*-
import numpy as np
from numpy.linalg import solve
from matplotlib import pyplot as plt

# 任意の3点から2次関数を決定する関数
# 引数     ：任意の3点A(x1, y1), B(x2, y2), C(x3, y3)
# 戻り値   ：y = ax **2 + bx + c の [a, b, c]
def DecisionQuadraticFunc(x1:int, y1:int, x2:int, y2:int, x3:int, y3:int) -> list:
    # 3元1次連立方程式を解く
    left_equation = np.array([[x1 ** 2, x1, 1], [x2 ** 2, x2, 1], [x3 ** 2, x3, 1]])
    right_equation = np.array([y1, y2, y3])

    result_data = solve(left_equation, right_equation)

    return result_data

# グラフを作成する関数
def MakeGraph(result_data:list, x1:int, y1:int, x2:int, y2:int, x3:int, y3:int) -> None:

    # 初期値をセット
    a = result_data[0]
    b = result_data[1]
    c = result_data[2]

    ########## 2次関数をグラフに図示 ##########
    # 2次関数のxを便宜上、0.1間隔で　-3 < x < 4 の範囲を指定
    xmin = -3
    xmax = 4
    xinterval = 0.1
    x = np.arange(xmin, xmax, xinterval)

    # yを算出
    y = a * (x ** 2) + b * x + c

    # グラフを作成
    plt.plot(x,y)
    ########################################

    ########## グラフにx軸,y軸から点Aまでを点線で図示 ##########
    # 補助線を点線で作成　[hlines：水平　vlines:垂直]
    plt.hlines([y1], 0, x1, "gray", linestyles='dashed')
    plt.vlines([x1], 0, y1, "gray", linestyles='dashed')
    #######################################################

    ########## グラフにx軸,y軸から点Bまでを点線で図示 ##########
    # 補助線を点線で作成　[hlines：水平　vlines:垂直]
    plt.hlines([y2], 0, x2, "gray", linestyles='dashed')
    plt.vlines([x2], 0, y2, "gray", linestyles='dashed')
    #######################################################

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
    # A(1, 4), B(-2, 10), C(3, 10)
    x1 = 1
    y1 = 4
    x2 = -2
    y2 = 10
    x3 = 3
    y3 = 10


    # x任意の3点から二次関数を求める
    result_data = DecisionQuadraticFunc(x1, y1, x2, y2, x3, y3)


    print('二次関数：y = '+ str(result_data[0]) + 'x**2 + (' \
                        + str(result_data[1]) + ')x + (' \
                        + str(result_data[2]) + ')')

    # グラフの作成
    MakeGraph(result_data, x1, y1, x2, y2, x3, y3)
