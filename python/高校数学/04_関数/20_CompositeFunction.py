# -*- Coding:UTF-8 -*-
import sympy

# f(x) = x + 1
def f(x):
    return x + 1

# g(x) = x**2
def g(x):
    return x ** 2

# h(x) = x - 3
def h(x):
    return x - 3

if __name__ == '__main__':
    # 文字列をセット
    x = sympy.Symbol('x')

    # 問題1：f○g(x) = f(g(x))
    print('問題1：', f(g(x)))

    # 問題2：g○f(x) = g(f(x))
    print('問題2：', g(f(x)))

    # 問題3：f○(g○h) = f(g(h(x)))
    print('問題3：', f(g(h(x))))
