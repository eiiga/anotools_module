# -*- Coding:UTF-8 -*-
import math

# 30度（度数法）をラジアン（弧度法）に変換
math_radian30 = math.radians(30)

print('30°->ラジアン = ', math_radian30)

# sin30, cos30, tan30をそれぞれ算出
math_sin30 = math.sin(math_radian30)
math_cos30 = math.cos(math_radian30)
math_tan30 = math.tan(math_radian30)

# sin30°は0.5だが、計算誤差が生じる
print('sin30° = ', math_sin30)
print('cos30° = ', math_cos30)
print('tan30° = ', math_tan30)

# 便宜上少数第2位まで表示
print('sin30° = ', round(math_sin30, 2))
print('cos30° = ', round(math_cos30, 2))
print('tan30° = ', round(math_tan30, 2))


# 60度（度数法）をラジアン（弧度法）に変換
math_radian60 = math.radians(60)

print('60°->ラジアン = ', math_radian60)

# sin60, cos60, tan60をそれぞれ算出
math_sin60 = math.sin(math_radian60)
math_cos60 = math.cos(math_radian60)
math_tan60 = math.tan(math_radian60)

# cos60°は0.5だが、計算誤差が生じる
print('sin60° = ', math_sin60)
print('cos60° = ', math_cos60)
print('tan60° = ', math_tan60)

# 便宜上少数第2位まで表示
print('sin60° = ', round(math_sin60, 2))
print('cos60° = ', round(math_cos60, 2))
print('tan60° = ', round(math_tan60, 2))


# 45度（度数法）をラジアン（弧度法）に変換
math_radian45 = math.radians(45)

print('45°->ラジアン = ', math_radian45)

# sin45, cos45, tan45をそれぞれ算出
math_sin45 = math.sin(math_radian45)
math_cos45 = math.cos(math_radian45)
math_tan45 = math.tan(math_radian45)

# tan45°は1だが、計算誤差が生じる
print('sin45° = ', math_sin45)
print('cos45° = ', math_cos45)
print('tan45° = ', math_tan45)

# 便宜上少数第2位まで表示
print('sin45° = ', round(math_sin45, 2))
print('cos45° = ', round(math_cos45, 2))
print('tan45° = ', round(math_tan45, 2))
