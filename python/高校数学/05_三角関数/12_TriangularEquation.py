# -*- Coding:UTF-8 -*-
import sympy

# 0≦x≦2πの範囲の値のみを配列に格納する関数
# 引数：配列
# 戻り値：配列
def ZeroTo2Pi(ans:list) -> list:

    # 戻り値用の配列をセット
    result  = []
    # πラジアンをセット
    pi = sympy.pi

    # 引数の配列分、ループ処理を行う
    for i in range(len(ans)):
        # 配列の要素が0以上かつ2π以下の結果のみを戻り値用の配列に格納する
        if ans[i] >= 0 and ans[i] <= 2 * pi:
            result.append(ans[i])

    return result

if __name__ == '__main__':

    # 文字列をセット
    x = sympy.Symbol('x')

    # 問題1：2sinx - 1 = 0
    ans1 = sympy.solve(2 * sympy.sin(x) - 1, x)
    print('計算結果（全量）：', ans1)
    print('計算結果（0≦x≦2π）：', ZeroTo2Pi(ans1))

    # 問題2：cos2x + cosx = 0
    ans2 = sympy.solve(sympy.cos(2 * x) + sympy.cos(x), x)
    print('計算結果（全量）：', ans2)
    print('計算結果（0≦x≦2π）：', ZeroTo2Pi(ans2))
