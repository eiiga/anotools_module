# -*- Coding:UTF-8 -*-
import math

# ▼問題1
ques1 = 2 ** 100

print('問題1')
print(ques1)
# 小数点以下切り捨て、1を加算
print(int(math.log10(ques1) + 1))


# ▼問題2
ques2 = (1/2) ** 10

print('問題2')
print(ques2)
# 小数点以下切り捨て、1で引く
print(int(math.log10(ques2) - 1))
