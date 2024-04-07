import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


# 先頭をインデックスとしてCSV読み込み
input_data = pd.read_csv('data.csv', index_col=0)

# インデックスを取得：年
year_rows = list(input_data.index)
kind_columns = list(input_data.columns)
datas = input_data.to_numpy()

colors = plt.cm.BuPu(np.linspace(0, 0.5, len(year_rows)))
n_rows = len(datas)

index = np.arange(len(kind_columns)) + 0.3
bar_width = 0.4

# Initialize the vertical-offset for the stacked bar chart.
y_offset = np.zeros(len(kind_columns))

# Plot bars and create text labels for the table
cell_text = []
for row in range(n_rows):
    plt.bar(index,
        datas[row],
        bar_width,
        bottom=y_offset,
        color=colors[row])
    y_offset = y_offset + datas[row]
    cell_text.append([x for x in datas[row]])
# Reverse colors and text labels to display the last value at the top.
cell_text.reverse()
year_rows.reverse()
colors = colors[::-1]

# Add a table at the bottom of the axes
plt.table(cellText=cell_text,
    rowLabels=year_rows,
    rowColours=colors,
    colLabels=kind_columns,
    loc='bottom')

# Adjust layout to make room for the table:
plt.subplots_adjust(left=0.2, bottom=0.2)

plt.ylabel("amount")
plt.xticks([])

plt.show()
