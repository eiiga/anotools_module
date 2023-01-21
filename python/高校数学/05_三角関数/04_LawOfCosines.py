# -*- Coding:UTF-8 -*-
import math

# 初期値の設定
b = 3
c = 4
A = 60

# 角度をラジアンに変換
radianA = math.radians(A)

# 余弦定理、a**2 = b**2 + c**2 - 2bccosAより
a_2 = b**2 + c**2 - (2 * b * c * math.cos(radianA))

# a > 0よりa_2(a**2)の値は正のみ
a = math.sqrt(a_2)

print('a = ', a)
