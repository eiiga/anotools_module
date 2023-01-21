
# 順列を計算する関数
def cal_permutation(n: int, r: int) -> int:
    # 戻り値の初期値をセット
    result = 1

    # nPrのうち、r回数分ループする
    for _ in range(r):
        # nPrのうち、nで掛け算
        result = result * n

        # デクリメント処理
        n = n - 1

    # 戻り値を返す
    return result


if __name__ == '__main__':
    # 問1
    print('問1：', cal_permutation(5, 3), '通り')

    # 問2-1
    print('問2-1：', cal_permutation(5, 5), '通り')

    # 問2-2
    parents_patern = cal_permutation(2, 2)
    children_patern = cal_permutation(3, 3)
    ans = parents_patern * children_patern
    print('問2-2：', ans, '通り')
