# -*- Coding:UTF-8 -*-
import sympy
import math

# 今回の問題の回答は実数のみとする
# （虚数は含まない）

# ▼問題1
# log(a)81 = 4

# 回答1
a = sympy.Symbol('a')
ques1 = sympy.solve(a**4 - 81, a)
print('問題1：' + str(ques1))


# ▼問題2
# log(b)5 = -1/2

# 回答2
b = sympy.Symbol('b')
ques2 = sympy.solve(b**(-1/2) - 5, b)
print('問題2：' + str(round(ques2[0], 2)))


# ▼問題3
# log(2)243

# 回答3
ques3 = math.log(243, 3)
print('問題3：' + str(round(ques3)))


# ▼問題4
# log(2)1/8

# 回答4
ques4 = math.log(1/8, 2)
print('問題4：' + str(ques4))
