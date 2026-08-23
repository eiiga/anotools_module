import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.optimize import curve_fit


def sigmoid(x, a, b):
    """
    シグモイド関数
    x を (-∞, ∞) の範囲から (0, 1) の範囲に変換する関数。
    ロジスティック回帰では、この (0, 1) の出力値を「購入する確率」とみなす。

    a: カーブの傾き（大きいほど境目で急に立ち上がる）
    b: カーブの中心位置（左右にずらすオフセット）
    """
    return 1 / (1 + np.exp(-a * (x - b)))


# CSVを読み込む
# 1行目：「age」ラベル + 年齢の値が横並び
# 2行目：「buy」ラベル + 購入有無（0:未購入, 1:購入）が横並び
# → 先頭列をインデックスとして読み込み、転置（.T）することで
#   「age列」「buy列」を持つ縦持ちのテーブルに変換する
input_data = pd.read_csv('sigmoid_data/sigmoid_data.csv', header=None, index_col=0).T

# 年齢（説明変数）と購入有無（目的変数）を取り出す
ages = input_data['age'].to_numpy(dtype=float)
buys = input_data['buy'].to_numpy(dtype=float)

# 実データにシグモイド関数をフィッティングし、
# 最も当てはまりの良いパラメータ a, b を求める
(param_a, param_b), _ = curve_fit(sigmoid, ages, buys, p0=[1.0, np.mean(ages)])

# フィッティングしたシグモイド曲線を描画するためのx軸データを作成
x_line = np.linspace(ages.min() - 5, ages.max() + 5, 300)
y_line = sigmoid(x_line, param_a, param_b)

# 実データ（散布図）を描画
plt.scatter(ages, buys, color='navy', label='actual data (0:not purchased, 1:purchased)')

# フィッティングしたシグモイド曲線を描画
plt.plot(x_line, y_line, color='crimson', label=f'sigmoid fit (a={param_a:.2f}, b={param_b:.2f})')

# グラフの装飾
plt.title('Sigmoid Function Fit: Age vs Purchase')
plt.xlabel('age')
plt.ylabel('purchase probability')
plt.ylim(-0.1, 1.1)
plt.grid(True)
plt.legend()

# グラフの表示
plt.show()
