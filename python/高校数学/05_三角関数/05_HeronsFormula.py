# -*- Coding:UTF-8 -*-
import math

def HeronFormula(a, b, c):
    s = (a + b + c) / 2
    S = math.sqrt(s * (s - a) * (s - b) * (s - c))

    return S

# メイン処理
if __name__ == '__main__':

    # 三角形ABCの3辺がそれぞれ a = 3, b = 4, c = 5 の時、
    # 三角形ABCの面積を求める。
    a = 3
    b = 4
    c = 5

    print('三角形の面積：', HeronFormula(a, b, c))
