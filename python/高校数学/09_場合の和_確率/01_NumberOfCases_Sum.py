# サイコロA、Bの和を求め、
# 和が4の倍数である場合が何通りか算出する処理
def sum_number_of_caces():

    # 定数：2つのサイコロA、Bを定義
    DICE_A = [1, 2, 3, 4, 5, 6]
    DICE_B = [1, 2, 3, 4, 5, 6]

    # 合計値の初期値をセット
    sum = 0

    # 処理結果格納用の配列をセット
    result_data = []

    # サイコロAの目の数だけ繰り返し
    for i in DICE_A:
        # サイコロBの目の数だけ繰り返し
        for j in DICE_B:
            # サイコロA、Bの和を算出
            sum = i + j

            # サイコロの目の和が4の倍数の場合
            if sum % 4 == 0:
                # サイコロA、Bの値を出力
                print('サイコロA：', i, 'サイコロB：', j)
                # 2つのサイコロの和を出力
                print('サイコロA、Bの和：', sum)
                # 出力結果の区切りとして「*」を出力
                print('**********')

                # 配列にサイコロA、Bの和を格納
                result_data.append(sum)

    # 合計で何通りあるか出力
    print('答え：', len(result_data), '通り')


# メイン処理
if __name__ == '__main__':
    sum_number_of_caces()
