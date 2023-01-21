# -*- Cording:UTF-8 -*-
import math

# 変数宣言
a = 6
A = 45
B = 60

# 角度をラジアンに変換
radianA = math.radians(A)
radianB = math.radians(B)

# 正弦定理より、a/sinA = b/sinB より
b = (a / math.sin(radianA)) * math.sin(radianB)

print('辺bの長さは：', b)
