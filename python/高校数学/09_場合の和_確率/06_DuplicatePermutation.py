
# 重複順列を計算する関数
def cal_duplicate(n: int, r: int) -> int:
    # 重複順列を求める（nΠr）
    ans = n ** r

    return ans


# メイン処理
if __name__ == '__main__':
    # 問1：3人でじゃんけんする場合（3Π3）
    print('3人：', cal_duplicate(3, 3), '通り')

    # 問2：4人でじゃんけんする場合（3Π4）
    print('4人：', cal_duplicate(3, 4), '通り')
