# -*- coding: UTF-8 -*-

# 素数チェック関数
def ChkPrimeNum(num: int) -> list:
    # 初期値をセット
    prime_num = []

    # 1からnum+1までの値でループ
    for i in range(1, num+1):
        # カウンタの初期化
        count = 0
        # 各要素分ループ
        for j in range(1, i+1):
            # 割り切れるならばカウントアップ
            if i % j == 0:
                count = count + 1
            # カウントが2より大きければ終了
            if count > 2:
                break

        # 割り切れる値が2つならば素数
        if count == 2:
            prime_num.append(i)

    return prime_num


# 素因数分解の関数
def PrimeFactorization(num: int, listdata: list) -> list:

    # 初期値を設定
    work_num = num
    result_data = []
    count_num = listdata
    i = 0

    # ループ処理
    while True:
        # 元の値が割り切れたら計算処理＆リストに追加
        if work_num % count_num[i] == 0:
            work_num = work_num / count_num[i]
            result_data.append(count_num[i])
        else:
            # インクリメント処理
            i = i + 1

        # 元の値が割る値よりも小さくなれば終了
        if work_num < count_num[i]:
            break

    # リストを返す
    return result_data


if __name__ == '__main__':
    # 例題の値をセット
    sample_num = 1080

    # 例題の値までの素数を取得
    prime_num = ChkPrimeNum(sample_num)

    print('素数：' + str(prime_num))
    print('素因数分解結果：' + str(PrimeFactorization(sample_num, prime_num)))
