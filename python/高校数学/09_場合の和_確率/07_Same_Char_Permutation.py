import math


# 同じを含む順列を計算する関数
def same_permutation(list_data:list) -> int:
    # タプル型に変換し、同じものを削除
    taple_data = set(list_data)

    # 同じ個数の計算結果初期値
    same_count_result = 1

    # タプル型の要素数分繰り返し
    for i in taple_data:
        # 同じものがある場合
        if list_data.count(i) > 1:
            # 同じ個数の計算結果に階乗結果を追加(p! * q! * r!...)
            same_count_result = same_count_result * math.factorial(list_data.count(i))

    # リストの全量をセット
    count_all_data = len(list_data)

    # 場合の数を算出（n! / (p! * q! * r!...)）
    ans = math.factorial(count_all_data) / same_count_result

    return int(ans)


if __name__ == '__main__':
    q1 = [1,3,3,5,7,7]
    print('問1：', same_permutation(q1), '通り')

    q2 = ['a', 'n', 'o', 't', 'o', 'o', 'l', 's']
    print('問2：', same_permutation(q2), '通り')
