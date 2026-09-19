import matplotlib.pyplot as plt
import pandas as pd


def min_max_normalize(series: pd.Series) -> pd.Series:
    """
    Min-Maxノーマライゼーション（正規化）
    データを「最小値=0, 最大値=1」の範囲に変換する手法。

    計算式：(x - 最小値) / (最大値 - 最小値)

    特徴：
    - 値の範囲が必ず [0, 1] に収まるため、直感的にわかりやすい
    - 外れ値（極端に大きい/小さい値）があると、他のデータが
      狭い範囲に押し込められてしまい、影響を受けやすい
    """
    return (series - series.min()) / (series.max() - series.min())


def z_score_standardize(series: pd.Series) -> pd.Series:
    """
    Z-score標準化（スタンダーディゼーション）
    データを「平均=0, 標準偏差=1」の分布に変換する手法。

    計算式：(x - 平均値) / 標準偏差

    特徴：
    - 値の範囲は決まっていない（理論上は -∞〜∞）
    - 外れ値の影響がMin-Max正規化より小さい
    - 機械学習（回帰・SVM・ニューラルネットワークなど）の
      前処理として広く使われる
    """
    return (series - series.mean()) / series.std()


# CSVを読み込む
# 列：name（名前）, height_cm（身長cm）, weight_kg（体重kg）
# → 単位・スケールが異なる2つの数値列を持つデータ
input_data = pd.read_csv('normalization_data/normalization_data.csv')

# 正規化・標準化を行いたい数値列のみを対象とする
target_columns = ['height_cm', 'weight_kg']

# Min-Max正規化を適用した結果を格納するDataFrame
min_max_result = input_data.copy()
for column in target_columns:
    min_max_result[column] = min_max_normalize(input_data[column])

# Z-score標準化を適用した結果を格納するDataFrame
z_score_result = input_data.copy()
for column in target_columns:
    z_score_result[column] = z_score_standardize(input_data[column])

# 変換前後の値をコンソールに出力して比較できるようにする
print('=== 元データ（スケールがバラバラ） ===')
print(input_data)
print('\n=== Min-Max正規化後（0〜1の範囲に統一） ===')
print(min_max_result)
print('\n=== Z-score標準化後（平均0・標準偏差1に統一） ===')
print(z_score_result)

# 「身長」と「体重」を例に、正規化の前後でスケールがどう変わるかを可視化する
# 正規化前は単位（cmとkg）が違うためスケールが揃わず、
# 正規化後はどちらも同じ基準（0〜1など）で比較できることを確認する
fig, axes = plt.subplots(1, 3, figsize=(15, 5))

axes[0].scatter(input_data['height_cm'], input_data['weight_kg'], color='navy')
axes[0].set_title('Before Normalization (raw data)')
axes[0].set_xlabel('height_cm')
axes[0].set_ylabel('weight_kg')
axes[0].grid(True)

axes[1].scatter(min_max_result['height_cm'], min_max_result['weight_kg'], color='crimson')
axes[1].set_title('After Min-Max Normalization')
axes[1].set_xlabel('height_cm (0 to 1)')
axes[1].set_ylabel('weight_kg (0 to 1)')
axes[1].grid(True)

axes[2].scatter(z_score_result['height_cm'], z_score_result['weight_kg'], color='seagreen')
axes[2].set_title('After Z-score Standardization')
axes[2].set_xlabel('height_cm (mean 0, std 1)')
axes[2].set_ylabel('weight_kg (mean 0, std 1)')
axes[2].grid(True)

plt.tight_layout()
plt.show()
