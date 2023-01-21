# -*- Coding:UTF-8 -*-
import sympy
import numpy as np
from matplotlib import pyplot as plt

# 導関数を求めてグラフに図示


# 関数：f(x) = x**2 + x
def f(x):
    y = x**2 + x

    return y


# 導関数：f'(x) = 2x + 1
def f_d(x):
    y = 2 * x + 1

    return y


# 文字列をセット
h = sympy.Symbol('h')
x = sympy.Symbol('x')

# 導関数を求める
result = sympy.limit((f(x+h)-f(x))/h, h, 0)

print(f(x), 'の導関数は', result)


# グラフ作成
# 便宜上、-5から5までの値を0.1間隔で設定
x_min = -5
x_max = 5
x_interval = 0.1
x = np.arange(x_min, x_max, x_interval)
# 関数f(x)を格納する配列
y1 = []
# 導関数f'(x) を格納する配列
y2 = []
# それぞれ配列に格納していく(便宜上、nは0.1間隔でセット)
for i in range(len(x)):
    y1.append(f(x[i]))
    y2.append(f_d(x[i]))
# 関数f(x)のグラフを作成
plt.plot(x, y1)
# 導関数f'(x)のグラフを作成
plt.plot(x, y2)
# グラフにx軸,y軸（0）を図示
# 補助線（0）を作成　[axhline：水平　axvline:垂直]
plt.axhline(y=0, color="gray")
plt.axvline(x=0, color="gray")
# グラフを表示
plt.show()
