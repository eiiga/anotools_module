# 円順列を算出する関数
def CalCircularPermutation(n: int, r: int) -> int:
    # 戻り値の初期値をセット
    cal_data = 1
    # 計算用一時変数
    cal_tmp = n

    # nPrのうち、r回数分ループする
    for _ in range(r):
        # nPrのうち、n(cal_tmp)で掛け算
        cal_data = cal_data * cal_tmp

        # デクリメント処理
        cal_tmp = cal_tmp - 1

    # 重複分を削除
    cal_data = cal_data / n

    # 戻り値を返す
    return int(cal_data)


if __name__ == '__main__':
    print('問1：', CalCircularPermutation(6, 6), '通り')
    print('問2：', CalCircularPermutation(5, 5) * 2, '通り')
