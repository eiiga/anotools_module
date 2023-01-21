# -*- Coding:UTF-8 -*-
import math

# 積立預金の元利合計を算出するメソッド
def TsumitateYokin(a:int, r:int, n:int) -> int:

    # 等比数列の和の公式：
    # (a/r)*(1+r)*{(1+r)**n-1}
    ans = (a / r) * (1 + r) * ((1 + r)**n - 1)
    # 小数点以下は切り捨て
    return math.floor(ans)

if __name__ == '__main__':
    # 毎年4万円ずつ年利4％で5年間積み立てた場合
    a = 40000
    r = 0.04
    n = 5

    # 積立預金の元利合計を算出するメソッドを呼び出し
    result = TsumitateYokin(a, r, n)

    # 計算結果を出力
    print(result)
