from dataclasses import dataclass


# クラスを簡潔にデータ構造として定義
# 自動で __init__, __repr__, __eq__ などを生成
@dataclass
class Point:
    x: int
    y: int


if __name__ == '__main__':
    p = Point(1, 2)
    print(p)
