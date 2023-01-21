# 組合せを計算する関数
def cal_combination(n: int, r: int) -> int:
    # 一時変数にnとrを格納
    tmp_n = n
    tmp_r = r

    # nPrとr!の初期値をセット
    n_P_r = 1
    r_kaijo = 1

    # rの回数分繰り返し
    for _ in range(r):
        # nPrとr!の値を算出
        n_P_r = n_P_r * tmp_n
        r_kaijo = r_kaijo * tmp_r

        # 一時変数をデクリメント
        tmp_r -= 1
        tmp_n -= 1
    
    # nCrの計算
    n_C_r = n_P_r / r_kaijo

    # 戻り値を返す（int型）
    return int(n_C_r)


if __name__ == '__main__':
    # 問1：4人、3人、2人に分ける
    print('問1：', cal_combination(9, 4) * cal_combination(5, 3) * cal_combination(2, 2), '通り')

    # 問2：3人ずつを3つの部屋に入れる
    print('問2：', cal_combination(9, 3) * cal_combination(6, 3) * cal_combination(3, 3), '通り')
