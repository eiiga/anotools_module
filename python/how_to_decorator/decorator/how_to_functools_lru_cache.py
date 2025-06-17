from functools import lru_cache


# 再計算のコストが高い関数をキャッシュして高速化
@lru_cache(maxsize=128)
def fib(n):
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)


if __name__ == '__main__':
    # 高速に計算される
    print(fib(30))
