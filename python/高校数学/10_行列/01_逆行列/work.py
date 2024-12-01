import numpy as np

matrix2 = np.array([[-3, 4], [2, -3]])

print(matrix2.shape[0]) # 2: 配列の要素数

# [[0 1 2 3]
#  [4 5 6 7]]
matrix4 = np.arange(8).reshape(2,4)

print(matrix4.shape[0]) # 2: 配列の要素数

# [[ 0  1  2  3]
#  [ 4  5  6  7]
#  [ 8  9 10 11]]
matrix5 = np.arange(12).reshape(3,4)

print(matrix5.shape[0]) # 3: 配列の要素数


print('===================')

# 0埋め
print(np.zeros_like(matrix2, dtype=float))