# 地点ABCのルートを全て算出する処理
def cal_cases_A_B_C():
    # 定数を設定
    LIST_A = ['A1', 'A2']
    LIST_B = ['B1', 'B2', 'B3']

    # 結果格納用配列
    list_result = []

    # Aのルート分ループ
    for i in range(len(LIST_A)):
        # Bのルート分ループ
        for j in range(len(LIST_B)):
            # ABの道順を合算
            case_abc = LIST_A[i]+LIST_B[j]
            # 道順を表示
            print(case_abc)
            # 配列に格納
            list_result.append(case_abc)

    # 答え：配列の要素数を出力
    print('答え：', len(list_result), '通り')


# メイン処理
if __name__ == '__main__':
    cal_cases_A_B_C()
