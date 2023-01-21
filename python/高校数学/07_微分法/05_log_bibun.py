import sympy
import numpy as np
from matplotlib import pyplot as plt


# f(x)=log[2]x
def f(x):
    return sympy.log(x, 2)


# 関数f'(x)=1/xlog2
def f_d(x):
    return 1/(x * sympy.log(2))


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


# 文字列をセット
x = sympy.Symbol('x')

# (1)：f(x)=log[2]x
print(sympy.diff(sympy.log(x, 2)))

# (2)：f(x)=x-logx
# sympy.log()で底を省略すると、ネイピア数eを指定することになる
print(sympy.diff(x - sympy.log(x)))

# (3)：f(x)=log2x
print(sympy.diff(sympy.log(2 * x)))

# (4)：f(x)=log(3x+2)
print(sympy.diff(sympy.log(3 * x + 2)))

# (5)：f(x)=log(2x-1)
print(sympy.diff(sympy.log(2 * x - 1)))

# (6)：f(x)=log[5](x-1)
print(sympy.diff(sympy.log(x - 1, 5)))

MakeGraph()
