# -*- Coding:UTF-8 -*-
import math

# 辺ABの長さを変数に格納
AB = 4

# 60度（度数法）をラジアン（弧度法）に変換
radian60 = math.radians(60)

# sin60°とcos60°を求める
sin60 = math.sin(radian60)
cos60 = math.cos(radian60)

# 辺ACを算出
AC = AB * sin60

# 辺BCを算出
BC = AB * cos60

# 計算結果を表示(便宜上少数第2位まで)
print('AC = ', round(AC, 2))
print('BC = ', round(BC, 2))
