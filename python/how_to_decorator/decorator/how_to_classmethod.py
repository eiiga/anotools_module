class Person:
    def __init__(self, name):
        self.name = name

    # クラス自体を操作したいとき
    # （例：別のコンストラクタを定義したいとき）
    @classmethod
    def from_dict(cls, data):
        return cls(data["name"])


if __name__ == '__main__':
    p = Person.from_dict({"name": "太郎"})
    print(p.name)
