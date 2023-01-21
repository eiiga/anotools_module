# -*- Coding:UTF-8 -*-
import math

# 角度を変数に格納
degree = 60
degree_2 = degree * 2

# ラジアンに変換
radian = math.radians(degree)
radian_2 = math.radians(degree_2)

#問題1 sin2α = 2sinαcosα
result = 2 * math.sin(radian) * math.cos(radian)
result_2 = math.sin(radian_2)

print('問題1')
print('2sin60°cos60° = ', result)
print('sin120° = ', result_2)

#問題2 cos2α = 1 - 2(sinα ** 2)
result = 1 - 2 * (math.sin(radian) ** 2)
result_2 = math.cos(radian_2)

print('問題2')
print('1 - 2(sin60° ** 2) = ', result)
print('cos120° = ', result_2)

#問題3 tan2α = 2tanα / 1 - (tanα ** 2)
result = (2 * math.tan(radian)) / ( 1 - (math.tan(radian) ** 2))
result_2 = math.tan(radian_2)

print('問題3')
print('2tan60° / 1 - (tan60° ** 2) = ', result)
print('tan120° = ', result_2)
