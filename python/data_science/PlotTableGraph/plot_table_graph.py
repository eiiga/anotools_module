import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


# 先頭列をインデックスとしてCSV読み込み
input_data = pd.read_csv('data.csv', index_col=0)

# 行列を取得
year_rows       = list(input_data.index)
kind_columns    = list(input_data.columns)

# データ部を格納
datas = input_data.to_numpy()

# カラーマップの設定
colors = plt.cm.BuPu(np.linspace(0, 0.5, len(year_rows)))

# 行数を取得
n_rows = len(datas)

# グラフのインデックスと幅を設定
index = np.arange(len(kind_columns)) + 0.3
bar_width = 0.4

# 積み上げ棒グラフの垂直オフセットを初期化
y_offset = np.zeros(len(kind_columns))

# 棒グラフをプロットし、表のテキストラベルを作成する
cell_text = []
for row in range(n_rows):
    plt.bar(index,
        datas[row],
        bar_width,
        bottom=y_offset,
        color=colors[row])
    y_offset = y_offset + datas[row]
    cell_text.append([x for x in datas[row]])

# 色とテキストラベルを反転（降順）
cell_text.reverse()
year_rows.reverse()
colors = colors[::-1]

# x軸に表を追加
plt.table(cellText=cell_text,
    rowLabels=year_rows,
    rowColours=colors,
    colLabels=kind_columns,
    loc='bottom')

# 表のスペースを確保
plt.subplots_adjust(left=0.2, bottom=0.2)

# ｙ軸ラベルの設定
plt.ylabel("amount")

# x軸のメモリ設定をなしにする
plt.xticks([])

# グラフと表の表示
plt.show()
