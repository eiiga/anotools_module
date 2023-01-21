# -*- Coding:UTF-8 -*-

def SumTohiSuretsu(a:int, r:int, n:int) -> float:
    # 合計の初期値をセット
    sum = 0

    # rについて、1、1より小さい、1より大きいで条件分岐
    if r == 1:
        # 公式①
        sum = a * n
    elif r < 1:
        # 公式②
        sum = (a * (1 - (r ** n))) / (1 - r)
    elif r > 1:
        # 公式③
        sum = (a * ((r ** n) - 1)) / (r - 1)


    return sum

if __name__ == '__main__':
    # 問題1　初項：4、公比：1、第7項までの等比数列の和
    a1 = 4
    r1 = 1
    n1 = 7

    print(SumTohiSuretsu(a1, r1, n1))

    # 問題2　初項：7、公比：-3、第5項までの等比数列の和
    a2 = 7
    r2 = -3
    n2 = 5

    print(SumTohiSuretsu(a2, r2, n2))

    # 問題3　初項：2、公比：3、第10項までの等比数列の和
    a3 = 2
    r3 = 3
    n3 = 10

    print(SumTohiSuretsu(a3, r3, n3))
