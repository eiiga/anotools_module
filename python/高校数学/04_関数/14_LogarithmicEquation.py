# -*- Coding:UTF-8 -*-
import sympy

# 文字列をセット
x = sympy.Symbol('x')

# 問題1
ans1 = sympy.solve(sympy.log(x, 3) - sympy.log(4 - x, 3), x)

# 問題2
ans2 = sympy.solve(sympy.log(x + 8, 4) - sympy.log(x + 2, 2), x)

# 問題3
ans3 = sympy.solve(sympy.log(x - 2, 6) + sympy.log(x + 3, 6) - 1, x)

# 問題4
ans4 = sympy.solve(sympy.log(x, 2) ** 2 - 2 * sympy.log(x, 2) - 3, x)


print('問題1：x = ' + str(ans1))

print('問題2：x = ' + str(ans2))

print('問題3：x = ' + str(ans3))

print('問題4：x = ' + str(ans4))
