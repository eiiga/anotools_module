# -*- Coding:UTF-8 -*-
import sympy

# 文字列をセット
x = sympy.Symbol('x')

# 問題1
ques1 = sympy.solve(2**x - 8, x)
print('問題1：' + str(ques1))

# 問題2
ques2 = sympy.solve(9**x - 3 * 27**x, x)
print('問題2：' + str(ques2))

# 問題3
ques3 = sympy.solve(4**x - 3 * 2**(x + 1) - 16, x)
print('問題3：' + str(ques3))
