# -*- Coding:UTF-8 -*-
import sympy
import numpy as np
from matplotlib import pyplot as plt

# 関数f(x) = sinx + cosx


def f_1(x):
    return sympy.sin(x) + sympy.cos(x)

# 関数f`(x) = cosx - sinx


def f_1_d(x):
    return sympy.cos(x) - sympy.sin(x)


def MakeGraph():
    # 便宜上、-5から5までの値を0.1間隔で設定
    x_min = -5
    x_max = 5
    x_interval = 0.1
    x = np.arange(x_min, x_max, x_interval)
    # 関数f(x)を格納する配列
    y_1 = []
    # 導関数f'(x)を格納する配列
    y_1_d = []
    # それぞれ配列に格納していく(便宜上、nは0.1間隔でセット)
    for i in range(len(x)):
        y_1.append(f_1(x[i]))
        y_1_d.append(f_1_d(x[i]))
    # 関数f(x)のグラフを作成
    plt.plot(x, y_1, color='blue', label="f(x)")
    # 導関数f'(x)のグラフを作成
    plt.plot(x, y_1_d, color='orange', label="f`(x)")
    # グラフにx軸,y軸（0）を図示
    # 補助線（0）を作成　[axhline：水平　axvline:垂直]
    plt.axhline(y=0, color="gray")
    plt.axvline(x=0, color="gray")

    # ラベルの表示
    plt.legend(bbox_to_anchor=(1, 1), loc='upper left',
               borderaxespad=0, fontsize=8)
    # グラフを表示
    plt.show()


# 文字列をセット
x = sympy.Symbol('x')

print(sympy.diff(sympy.sin(x)))
print(sympy.diff(sympy.cos(x)))
print(sympy.diff(sympy.tan(x)))


print(sympy.diff(f_1(x)))

MakeGraph()
