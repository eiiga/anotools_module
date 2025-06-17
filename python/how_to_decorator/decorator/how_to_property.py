class Circle:
    def __init__(self, radius):
        self._radius = radius

    # 関数をフィールド（属性）のようにアクセス
    @property
    def area(self):
        return 3.14 * self._radius ** 2


if __name__ == '__main__':
    c = Circle(5)
    # 関数だが属性のようにアクセスできる: 「()」を使用しない
    print(c.area)
