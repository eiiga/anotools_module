# -*- Coding: UTF-8 -*-

import math

# 2次方程式：解の公式
def Solution(a:int, b:int, c:int) -> list:
    x = []
    x1 = (-b + math.sqrt(b ** 2 - 4 * a * c)) / (2 * a)
    x.append(x1)
    x2 = (-b - math.sqrt(b ** 2 - 4 * a * c)) / (2 * a)
    x.append(x2)

    return x


if __name__ == '__main__':
    # 例題①
    a = 1
    b = 3
    c = 2
    print(Solution(a, b, c))

    # 例題②
    a = 6
    b = -18
    c = -60
    print(Solution(a, b, c))

    # 例題③
    a = 2
    b = -16
    c = 30
    print(Solution(a, b, c))
