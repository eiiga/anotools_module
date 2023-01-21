# -*- Coding:UTF-8 -*-
import math

# 度数を変数に格納
degree = 165
tmp_degree1 = 120
tmp_degree2 = 45

# 度数をラジアンに変換
radian = math.radians(degree)
tmp_radian1 = math.radians(tmp_degree1)
tmp_radian2 = math.radians(tmp_degree2)

# 加法定理 tan(α+β)
result = math.tan(radian)

# 答え（少数第2位で表示）
print('tan(165°) = ', round(result, 2))

# 加法定理 (tanα + tanβ) / (1 - tanαtanβ)
result = (math.tan(tmp_radian1) + math.tan(tmp_radian2)) / (1 - math.tan(tmp_radian1) * math.tan(tmp_radian2))

# 答え（少数第2位で表示）
print('(tan120° + tan45°) / (1 - tan120°tan45°) = ', round(result, 2))

# 度数を変数に格納
degree = 15
tmp_degree1 = 60
tmp_degree2 = 45

# 度数をラジアンに変換
radian = math.radians(degree)
tmp_radian1 = math.radians(tmp_degree1)
tmp_radian2 = math.radians(tmp_degree2)

# 加法定理 tan(α-β)
result = math.tan(radian)

# 答え（少数第2位で表示）
print('tan(15°) = ', round(result, 2))

# 加法定理 (tanα - tanβ) / (1 + tanαtanβ)
result = (math.tan(tmp_radian1) - math.tan(tmp_radian2)) / (1 + math.tan(tmp_radian1) * math.tan(tmp_radian2))

# 答え（少数第2位で表示）
print('(tan60° - tan45°) / (1 + tan60°tan45°) = ', round(result, 2))
