# -*- Coding:UTF-8 -*-

# 等比数列の関数
# 引数
#   a：初項（int型）
#   r：公比（int型）
#   n：第N項まで（int型）
# 戻り値
#   等比数列の値（list型）
def tohisuretsu(a:int, r:int, n:int) -> list:

    # 空の配列をセット
    ans = []

    # ループ用初期値(ループカウンタ)
    i = 1

    # N番目の値が格納されるまで処理を繰り返す
    while len(ans) < n:
        # 等比数列の公式(a * r**(i-1))の結果を配列に格納
        ans.append(a * r**(i-1))

        i = i + 1

    # 戻り値として、配列を返す
    return ans


if __name__ == '__main__':
    a = 3
    r = -2
    n = 10

    result = tohisuretsu(a, r, n)

    print(result)
