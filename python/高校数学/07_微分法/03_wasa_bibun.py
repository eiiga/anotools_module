# -*- Coding:UTF-8 -*-
import sympy
import numpy as np
from matplotlib import pyplot as plt

# 導関数を求めてグラフに図示


# 関数：f(x) = 2x**3 - x**2 + 4x - 7
def f_1(x):
    y_1 = (2 * x**3) - (x**2) + (4 * x) - 7

    return y_1


# 関数：f(x) = -3/2x**4 + x**3 - x**2 + x - 7/5
def f_2(x):
    y_2 = (-3/2) * x**4 + (x**3) - (x**2) + x - (7/5)

    return y_2


# 導関数：f'(x) = 6x**2 - 2x + 4
def f_1_d(x):
    y_1_d = 6 * x**2 - 2 * x + 4

    return y_1_d


# 導関数：f'(x) = -6x**3 + 3x**2 - 2x + 1
def f_2_d(x):
    y_2_d = -6 * x**3 + 3 * x**2 - 2 * x + 1

    return y_2_d


# グラフ作成
def MakeGraph1():
    # 便宜上、-5から5までの値を0.1間隔で設定
    x_min = -5
    x_max = 5
    x_interval = 0.1
    x = np.arange(x_min, x_max, x_interval)
    # 関数f(x)を格納する配列
    y_1 = []
    # 導関数f'(x) を格納する配列
    y_1_d = []
    # それぞれ配列に格納していく(便宜上、nは0.1間隔でセット)
    for i in range(len(x)):
        y_1.append(f_1(x[i]))
        y_1_d.append(f_1_d(x[i]))
    # 関数f(x)のグラフを作成
    plt.plot(x, y_1)
    # 導関数f'(x)のグラフを作成
    plt.plot(x, y_1_d)
    # グラフにx軸,y軸（0）を図示
    # 補助線（0）を作成　[axhline：水平　axvline:垂直]
    plt.axhline(y=0, color="gray")
    plt.axvline(x=0, color="gray")
    # グラフを表示
    plt.show()


# グラフ作成
def MakeGraph2():
    # 便宜上、-5から5までの値を0.1間隔で設定
    x_min = -5
    x_max = 5
    x_interval = 0.1
    x = np.arange(x_min, x_max, x_interval)
    # 関数f(x)を格納する配列
    y_2 = []
    # 導関数f'(x)を格納する配列
    y_2_d = []
    # それぞれ配列に格納していく(便宜上、nは0.1間隔でセット)
    for i in range(len(x)):
        y_2.append(f_2(x[i]))
        y_2_d.append(f_2_d(x[i]))
    # 関数f(x)のグラフを作成
    plt.plot(x, y_2)
    # 導関数f'(x)のグラフを作成
    plt.plot(x, y_2_d)
    # グラフにx軸,y軸（0）を図示
    # 補助線（0）を作成　[axhline：水平　axvline:垂直]
    plt.axhline(y=0, color="gray")
    plt.axvline(x=0, color="gray")
    # グラフを表示
    plt.show()


if __name__ == '__main__':
    # 文字列をセット
    h = sympy.Symbol('h')
    x = sympy.Symbol('x')

    # 導関数を求める
    result_1 = sympy.limit((f_1(x+h)-f_1(x))/h, h, 0)
    result_2 = sympy.limit((f_2(x+h)-f_2(x))/h, h, 0)

    # 計算結果を表示
    print('問題1：', result_1)
    print('問題2：', result_2)

    # グラフを作成
    MakeGraph1()
    MakeGraph2()
