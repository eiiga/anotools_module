# -*- Coding:UTF-8 -*-

# 自然数の累乗の和の公式
# 引数：n項
# 戻り値：自然数の累乗の和
def func_ruijo(n:int):

    # Σ K(n, k=1) = 1/2n(n+1)
    ans = (1 / 2) * n * (n + 1)

    # 計算結果を戻り値として返す。
    return ans

# 自然数の累乗の和の公式（2乗）
# 引数：n項
# 戻り値：自然数の累乗の和（2乗）
def func_ruijo_2(n:int):
    # Σ K**2(n, k=1) = 1/6n(n+1)(2n+1)
    ans = (1 / 6) * n * (n + 1) * (2 * n + 1)

    return ans

# 自然数の累乗の和の公式（3乗）
# 引数：n項
# 戻り値：自然数の累乗の和（3乗）
def func_ruijo_3(n:int):
    # Σ K**3(n, k=1)
    ans = ((1 / 2) * n * (n + 1)) ** 2

    return ans


# メイン処理
if __name__ == '__main__':
    # 問題1：Σ 2K(n=6, k=1)
    ans1 = 2 * (func_ruijo(6))
    print('問題1：', ans1)

    #問題2：Σ K**2(n=10, k=1)
    ans2 = func_ruijo_2(10)
    print('問題2：', ans2)

    #問題2：Σ K**3(n=7, k=1)
    ans3 = func_ruijo_3(7)
    print('問題3：', ans3)

    # 問題4：Σ (2K-1)**2(n=5, k=1) = Σ (4k**2 - 4K + 1)(n=5, k=1)
    ans4 = (4 * func_ruijo_2(5)) - (4 * func_ruijo(5)) + 5
    print('問題4：', ans4)
