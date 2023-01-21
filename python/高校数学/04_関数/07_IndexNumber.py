# -*- Coding:UTF-8 -*-
import sympy

if __name__ == '__main__':
    # 文字列をセット
    x = sympy.Symbol('x')
    y = sympy.Symbol('y')

    # 問題1
    print('問題1：' + str((x ** 2) * (x ** 3)))

    # 問題2
    print('問題2：' + str((x ** 5) / (x ** 3)))

    # 問題3
    print('問題3：' + str((x ** 3) ** 2))

    # 問題4
    print('問題4：' + str((x * y) ** 3))
