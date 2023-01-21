# -*- Coding:UTF-8 -*-
import math

# 度数を変数に格納
degree = 105
tmp_degree1 = 45
tmp_degree2 = 60

# 度数をラジアンに変換
radian = math.radians(degree)
tmp_radian1 = math.radians(tmp_degree1)
tmp_radian2 = math.radians(tmp_degree2)

# 加法定理 sin(α+β)
result = math.sin(radian)

# 答え（少数第2位で表示）
print('sin(105°) = ', round(result, 2))

# 加法定理 sinαcosβ + cosαsinβ
result = math.sin(tmp_radian1) * math.cos(tmp_radian2) + math.cos(tmp_radian1) * math.sin(tmp_radian2)

# 答え（少数第2位で表示）
print('sin45°cos60° + cos45°sin60° = ', round(result, 2))

# 度数を変数に格納
degree = 15
tmp_degree1 = 45
tmp_degree2 = 30

# 度数をラジアンに変換
radian = math.radians(degree)
tmp_radian1 = math.radians(tmp_degree1)
tmp_radian2 = math.radians(tmp_degree2)

# 加法定理 sin(α-β)
result = math.sin(radian)

# 答え（少数第2位で表示）
print('sin(15°) = ', round(result, 2))

# 加法定理 sinαcosβ - cosαsinβ
result = math.sin(tmp_radian1) * math.cos(tmp_radian2) - math.cos(tmp_radian1) * math.sin(tmp_radian2)

# 答え（少数第2位で表示）
print('sin45°cos30° - cos45°sin30° = ', round(result, 2))
