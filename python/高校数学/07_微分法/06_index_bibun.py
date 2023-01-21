import sympy
import numpy as np
from matplotlib import pyplot as plt


# f(x) = 2 ** (3x)
def f(x):
    return 2 ** (3 * x)


# 関数f'(x)=3*2**(3*x)*log(2)
def f_d(x):
    return 3 * 2 ** (3 * x) * sympy.log(2)


def MakeGraph():
    # 便宜上、0.1から5までの値を0.1間隔で設定
    x_min = 0.1
    x_max = 5
    x_interval = 0.1
    x = np.arange(x_min, x_max, x_interval)

    # 関数f(x)を格納する配列
    y = []
    # 導関数f'(x)を格納する配列
    y_d = []

    # それぞれ配列に格納していく(便宜上、nは0.1間隔でセット)
    for i in range(len(x)):
        y.append(f(x[i]))
        y_d.append(f_d(x[i]))

    # 関数f(x)のグラフを作成
    plt.plot(x, y, color='blue', label="f(x)")

    # 導関数f'(x)のグラフを作成
    plt.plot(x, y_d, color='orange', label="f`(x)")

    # グラフにx軸,y軸（0）を図示
    # 補助線（0）を作成　[axhline：水平　axvline:垂直]
    plt.axhline(y=0, color="gray")
    plt.axvline(x=0, color="gray")

    # ラベルの表示
    plt.legend(bbox_to_anchor=(1, 1), loc='upper left',
               borderaxespad=0, fontsize=8)

    # グラフを表示
    plt.show()


if __name__ == '__main__':

    # 文字列をセット
    x = sympy.Symbol('x')

    # (1)f(x) = 2 ** (3x)
    print('問題1：', sympy.diff(2 ** (3 * x)))

    # (2)f(x) = e ** (2x)
    print('問題2：', sympy.diff(sympy.exp(2 * x)))

    # (3)f(x) = e ** (-x ** 2)
    print('問題3：', sympy.diff(sympy.exp(-x ** 2)))

    # (4)f(x) = xe ** (x)
    print('問題4：', sympy.diff(x * sympy.exp(x)))

    MakeGraph()
