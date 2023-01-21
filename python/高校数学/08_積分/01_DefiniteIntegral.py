import sympy
import numpy as np
from matplotlib import pyplot as plt


def MakeGraph():
    # 便宜上、-3から3までの値を0.1間隔で設定
    x_min = -3
    x_max = 3
    x_interval = 0.1
    x_val = np.arange(x_min, x_max, x_interval)

    # 積分の範囲(1から2まで)
    integral_x = np.arange(1, 2.1, 0.1)

    # 関数f(x)を格納する配列
    y_val = []
    integral_y = []

    # それぞれ配列に格納していく(便宜上、nは0.1間隔でセット)
    for i in x_val:
        y_val.append(9 * i ** 2 - 4 * i + 3)

    for i in integral_x:
        integral_y.append(9 * i ** 2 - 4 * i + 3)

    # 関数f(x)のグラフを作成
    plt.plot(x_val, y_val, color='blue', label="f(x)")

    # グラフにx軸,y軸（0）を図示
    # 補助線（0）を作成　[axhline：水平　axvline:垂直]
    plt.axhline(y=0, color="gray")
    plt.axvline(x=0, color="gray")

    # ラベルの表示
    plt.legend(bbox_to_anchor=(1, 1), loc='upper left',
               borderaxespad=0, fontsize=8)

    # xの値が1から2までの範囲を塗りつぶす
    plt.fill_between(integral_x, integral_y, facecolor='red')

    # グラフを表示
    plt.show()


# 文字列の定義
x = sympy.Symbol('x')

# 問題(1)の式をセット
formula1 = 9 * x ** 2 - 4 * x + 3
# integrateを使用して積分を計算（1から2まで）
ans1 = sympy.integrate(formula1, (x, 1, 2))
# 計算結果を出力
print('問題1：', ans1)

# 問題(2)の式をセット
formula2 = (3 * x - 1) * (x + 1)
# integrateを使用して積分を計算（1から3まで）
ans2 = sympy.integrate(formula2, (x, 1, 3))
# 計算結果を出力
print('問題2：', ans2)

# 問題(3)の式をセット
formula3 = (8 / 3) * x ** 3 + x - 1
# integrateを使用して積分を計算（-1から2まで）
ans3 = sympy.integrate(formula3, (x, -1, 2))
# 計算結果を出力
print('問題3：', round(ans3, 2))

MakeGraph()
