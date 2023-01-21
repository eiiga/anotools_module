# -*- Coding:UTF-8 -*-

# 等差数列の和を算出する関数(初項・項数・公差ver)
# 引数
#   a：初項(int)
#   d：公差(int)
#   n：項数(int)
# 戻り値
#   等差数列の和(float)
def Sum_a_d_n(a:int, d:int, n:int) -> float:

    # 等差数列の和の公式
    sum = (n * (2 * a + (n - 1) * d)) / 2

    # 戻り値として、等差数列の和を返す
    return sum


# 等差数列の和を算出する関数(初項・項数・末項ver)
# 引数
#   a：初項(int)
#   l：末項(int)
#   n：項数(int)
# 戻り値
#   等差数列の和(float)
def Sum_a_l_n(a:int, l:int, n:int) -> float:

    # 等差数列の和の公式
    sum = (n * (a + l)) / 2

    # 戻り値として、等差数列の和を返す
    return sum

# メイン処理
if __name__ == '__main__':
    # (1)初項：2、公差：3、項数：17の等差数列の和
    a = 2
    d = 3
    n = 17

    # 等差数列関数を呼び出し結果を格納
    result = Sum_a_d_n(a, d, n)

    # 結果を表示する
    print(result)

    # (2)初項：10、末項：-32、項数：15の等差数列の和
    a = 10
    l = -32
    n = 15

    # 等差数列関数を呼び出し結果を格納
    result = Sum_a_l_n(a, l, n)

    # 結果を表示する
    print(result)
