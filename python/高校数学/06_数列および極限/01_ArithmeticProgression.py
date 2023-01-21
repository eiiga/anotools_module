# -*- Coding:UTF-8 -*-
import numpy as np

# 等差数列の関数
# 引数
#   a：初項
#   d：公差
#   n：N番目まで繰り返す用の値
def ArithmeticalProgression(a:int, d:int, n:int) -> list:

    # ループ用初期値(ループカウンタ)
    i = 1

    # 戻り値用配列をセット
    ans = []

    # N番目の値が格納されるまで処理を繰り返す
    while len(ans) < n:
        # 等差数列の公式(a + (i - 1)d)の結果を配列に格納
        ans.append(a + (i - 1) * d)

        # ループカウンタをインクリメントする
        i = i + 1

    # 戻り値として、配列を返す
    return ans

# メイン処理
if __name__ == '__main__':
    # 初項：3、公差：4、10番目まで値を取得
    a = 3
    d = 4
    n = 10

    # 等差数列関数を呼び出し結果を格納
    result = ArithmeticalProgression(a, d, n)

    # 結果を表示する
    print(result)

    ans_range = [i for i in range(a, 40, d)]
    print(ans_range)

    ans_numpy = np.arange(a, 40, d)
    print(ans_numpy)
