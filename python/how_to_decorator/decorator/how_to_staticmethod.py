class Math:
    # インスタンス (self) やクラス (cls) に関係ない
    # ユーティリティ関数的なメソッドを定義
    @staticmethod
    def add(x, y):
        return x + y


if __name__ == '__main__':
    print(Math.add(3, 5))
