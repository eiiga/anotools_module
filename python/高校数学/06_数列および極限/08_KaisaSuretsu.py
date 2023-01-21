# -*- Coding:UTF-8 -*-

# 初期値をセット
a_array = [2, 4, 8, 14, 22, 32]
b_array = []
i = 0

# 配列(a_array)の要素数-1回分繰り返し
while i < len(a_array) - 1:
    # 配列(a_array)の[i+1]番目の要素 - [i]番目の要素の結果を配列(b_array)に格納
    b_array.append(a_array[i+1] - a_array[i])
    # インクリメント処理
    i += 1

print('an：', a_array)
print('bn：', b_array)


# 数列(an)の第10項の値を求める

# 初期値:項数[N:10項]
N = 10

# 配列(b_array)関係の値
# 初項(b1)と公差(d)を変数に格納
# 数列(an)の第10項-1(=第9項)
b1 = b_array[0]
d = b_array[1] - b_array[0]
n = N - 1

# 配列(b_array)の値を加算する(等差数列の和の公式)
a10 = a_array[0] + ((n * (2 * b1 + (n - 1) * d)) / 2)

print('階差数列の第10項：', a10)


# 数列(an)の第10項までの合計値を求める
sum = 0
j = 0

# 10回繰り返し
for j in range(N):
    sum = sum + a_array[0] + ((j * (2 * b1 + (j - 1) * d)) / 2)

print('階差数列の第10項までの和：', sum)
