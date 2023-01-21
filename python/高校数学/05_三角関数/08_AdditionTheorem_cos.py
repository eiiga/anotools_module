# -*- Coding:UTF-8 -*-
import math

# 度数を変数に格納
degree = 15
tmp_degree1 = 60
tmp_degree2 = 45

# 度数をラジアンに変換
radian = math.radians(degree)
tmp_radian1 = math.radians(tmp_degree1)
tmp_radian2 = math.radians(tmp_degree2)

# 加法定理 cos(α-β)
result = math.cos(radian)

# 答え（少数第2位で表示）
print('cos(15°) = ', round(result, 2))

# 加法定理 cosαcosβ - sinαsinβ
result = math.cos(tmp_radian1) * math.cos(tmp_radian2) + math.sin(tmp_radian1) * math.sin(tmp_radian2)

# 答え（少数第2位で表示）
print('cos60°cos45° + sin60°sin45° = ', round(result, 2))

# 度数を変数に格納
degree = 75
tmp_degree1 = 45
tmp_degree2 = 30

# 度数をラジアンに変換
radian = math.radians(degree)
tmp_radian1 = math.radians(tmp_degree1)
tmp_radian2 = math.radians(tmp_degree2)

# 加法定理 cos(α+β)
result = math.cos(radian)

# 答え（少数第2位で表示）
print('cos(75°) = ', round(result, 2))

# 加法定理 cosαcosβ - sinαsinβ
result = math.cos(tmp_radian1) * math.cos(tmp_radian2) - math.sin(tmp_radian1) * math.sin(tmp_radian2)

# 答え（少数第2位で表示）
print('cos45°cos30° - sin45°sin30° = ', round(result, 2))
