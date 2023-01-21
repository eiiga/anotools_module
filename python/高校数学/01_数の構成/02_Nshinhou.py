# -*- coding: UTF-8 -*-

# アルファベットを数字に変換する関数（16進法まで）
def Check_A_To_Num(num:str) -> str:
    if num == 'A':
        return '10'
    elif num == 'B':
        return '11'
    elif num == 'C':
        return '12'
    elif num == 'D':
        return '13'
    elif num == 'E':
        return '14'
    elif num == 'F':
        return '15'
    else:
        return num

# N進法を10進法に変換する関数
def ChangeNTo10(num:str, N:int) -> int:
    # 引数「num」をlist関数にて1文字ずつに分割し配列に格納
    before_num = list(num)
    # 初期値をセット
    after_num = 0

    # ループ処理（1から配列の要素数＋1まで）
    for i in range(1, len(before_num) + 1):
        # アルファベットを数字に変換する関数（16進法まで）を呼び出し変数に格納
        # -iを使用し、リストの逆順（1の位）から要素を取得
        tmp_num = str(Check_A_To_Num(before_num[-i]))
        # 計算処理（各位の値をN進法から10進法に変換）
        tmp_cal = int(tmp_num)*(N ** (i - 1))
        # 各位の値をを合算
        after_num = after_num + tmp_cal

    return after_num


# 数字をアルファベットに変換する関数（16進法まで）
def Check_Num_To_A(num:int) -> str:
    if num == 10:
        return 'A'
    elif num == 11:
        return 'B'
    elif num == 12:
        return 'C'
    elif num == 13:
        return 'D'
    elif num == 14:
        return 'E'
    elif num == 15:
        return 'F'
    else:
        return str(num)

# 10進法をN進法に変換する関数
def Change10ToN(num:int, N:int) -> str:
    # 初期値をセット
    after_num = ''
    cal_num = num

    # 変換対象の値が0未満になるまでループ処理
    while cal_num > 0:
        # 余りを取得
        tmp_cal = cal_num % N
        # 取得した余りについて、
        # 数字をアルファベットに変換（16進法まで）
        tmp_num = Check_Num_To_A(tmp_cal)

        # 変換した値を文字列で連結
        after_num = tmp_num + after_num

        # 変換対象の値について、商のみを取得
        cal_num = cal_num // N

    return after_num

# メイン処理
if __name__ == '__main__':
    str_num = '1201'
    N = 3
    print(ChangeNTo10(str_num, N))

    str_num = '231'
    N = 4
    print(ChangeNTo10(str_num, N))

    str_num = 'FF'
    N = 16
    print(ChangeNTo10(str_num, N))



    int_num = 46
    N = 3
    print(Change10ToN(int_num, N))

    int_num = 45
    N = 4
    print(Change10ToN(int_num, N))

    int_num = 255
    N = 16
    print(Change10ToN(int_num, N))
