
# 紙幣＆貨幣リスト
MONEY_LIST = [10000, 5000, 1000, 500, 100, 50, 10, 5, 1]

# 試験用合計金額リスト
TOTAL_MONEY_LIST = [
    73735, 9561, 4950, 600, 70590,
    117440, 2350, 0, 52318, 12524,
    55220, 510546, -6632, 523871
    ]


# 最小枚数を計算する処理
def cal_minimum_number(total_money):
    # 返却用辞書型
    dict_result = {}

    # 紙幣＆貨幣リスト分繰り返し
    for money in MONEY_LIST:
        # 紙幣＆貨幣カウンタの初期値セット
        count = 0

        # 合計金額が紙幣、貨幣以上の場合繰り返し
        while total_money >= money:
            # 合計金額を減算
            total_money -= money
            # カウンタインクリメント
            count += 1

        # 結果を返却用辞書型にセット
        dict_result[money] = count

    # 結果を返す
    return dict_result


# メイン処理
if __name__ == '__main__':
    # 試験用合計金額リスト
    for total_money in TOTAL_MONEY_LIST:
        # 最小枚数の結果を取得
        result = cal_minimum_number(total_money)

        # 最小枚数の結果を表示
        print(total_money, result)
