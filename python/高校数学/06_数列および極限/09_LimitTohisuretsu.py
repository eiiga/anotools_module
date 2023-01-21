# -*- Coding:UTF-8 -*-
import sympy
import numpy as np
from matplotlib import pyplot as plt


def MakeGraph():
    # 便宜上、第1から100項までの値を設定
    n_min = 1
    n_max = 100
    n_interval = 1
    n = np.arange(n_min, n_max, n_interval)

    # y = x**3 - 4 * x**2
    # y = (1-x**2)/(3 * x + 1)

    # ルートの計算はそのままできないのでループ処理で各要素を入れる
    # y = []
    # for i in range(len(x)):
    #     y.append(sympy.sqrt(x[i] - 1) - sympy.sqrt(x[i]))

    # y = (4/3)**x
    # y = (-2/3)**x
    # y = (3**x) - (2**x)
    # y = ((3**x) - (2**x))/((2**x) + (3**x))

    # dn = (-1)**n

    an = n**3 - 4 * n**2

    # グラフを作成
    plt.plot(n, an)

    # グラフにx軸,y軸（0）を図示
    # 補助線（0）を作成　[axhline：水平　axvline:垂直]
    plt.axhline(y=0, color="gray")
    plt.axvline(x=0, color="gray")

    # グラフを表示
    plt.show()


# 文字列をセット
n = sympy.Symbol('n')

# 無限をセット
oo = sympy.oo

ans1 = sympy.limit((n**3) - (4 * (n**2)), n, oo)
ans2 = sympy.limit((1 - (n**2))/((3 * n) + 1), n, oo)
ans3 = sympy.limit(((3**n) - (2**n))/((2**n) + (3**n)), n, oo)
ans4 = sympy.limit((-1)**n, n, oo)

print(ans1)
print(ans2)
print(ans3)
print(ans4)
MakeGraph()

# ans1 = sympy.limit(x**3 - 4 * x**2, x, oo)
# ans2 = sympy.limit((1-x**2)/(3 * x + 1), x, oo)
# ans3 = sympy.limit(sympy.sqrt(x - 1) - sympy.sqrt(x), x, oo)
# ans4 = sympy.limit((4/3)**x, x, oo)
# ans5 = sympy.limit((-2/3)**x, x, oo)
# ans6 = sympy.limit((3**x) - (2**x), x, oo)
# ans7 = sympy.limit(((3**x) - (2**x))/((2**x) + (3**x)), x, oo)
#
# print(ans1)
# print(ans2)
# print(ans3)
# print(ans4)
# print(ans5)
# print(ans6)
# print(ans7)
# MakeGraph()
