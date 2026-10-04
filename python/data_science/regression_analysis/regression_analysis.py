import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def simple_linear_regression(x: pd.Series, y: pd.Series) -> tuple[float, float]:
    """
    単回帰分析（最小二乗法）
    1つの説明変数 x から目的変数 y を予測する直線「y = a * x + b」を求める。

    - a：傾き（回帰係数）… x が1増えると y がどれだけ増えるか
    - b：切片 … x が0のときの y の値

    最小二乗法とは：
    実際の値 y と、直線で予測した値との「ズレ（残差）」を2乗して合計し、
    その合計が最も小さくなるように a と b を決める方法。
    （2乗するのは、プラスのズレとマイナスのズレが打ち消し合わないようにするため）

    計算式：
    - a = Σ(x - xの平均)(y - yの平均) / Σ(x - xの平均)^2
          （= xとyの共分散 / xの分散）
    - b = yの平均 - a * xの平均
    """
    x_mean = x.mean()
    y_mean = y.mean()

    # 分子：x と y が「一緒にどう動くか」を表す量（共分散に相当）
    numerator = ((x - x_mean) * (y - y_mean)).sum()
    # 分母：x が「どれだけばらついているか」を表す量（分散に相当）
    denominator = ((x - x_mean) ** 2).sum()

    slope = numerator / denominator
    intercept = y_mean - slope * x_mean
    return slope, intercept


def multiple_linear_regression(x: pd.DataFrame, y: pd.Series) -> np.ndarray:
    """
    重回帰分析（最小二乗法・正規方程式）
    複数の説明変数 x1, x2, ... から目的変数 y を予測する式
    「y = b0 + b1 * x1 + b2 * x2 + ...」の係数を求める。

    行列を使うと、最小二乗法の解は次の「正規方程式」で一度に求められる：
        β = (XᵀX)⁻¹ Xᵀy
    - X：説明変数を並べた行列（先頭列に切片用の「1」の列を追加する）
    - Xᵀ：X の転置（行と列を入れ替えた行列）
    - ⁻¹：逆行列

    戻り値：[b0（切片）, b1, b2, ...] の順に並んだ係数の配列
    """
    # 切片 b0 を計算するために、すべて1の列を先頭に追加する
    # （b0 * 1 = b0 となるので、切片も他の係数と同じように計算できる）
    ones = np.ones((len(x), 1))
    x_matrix = np.hstack([ones, x.to_numpy()])
    y_vector = y.to_numpy()

    # 逆行列を直接計算する（np.linalg.inv）よりも、
    # 連立方程式として解く（np.linalg.solve）方が数値計算的に安定している
    xtx = x_matrix.T @ x_matrix
    xty = x_matrix.T @ y_vector
    return np.linalg.solve(xtx, xty)


def r_squared(y_actual: pd.Series, y_predicted: pd.Series) -> float:
    """
    決定係数（R²）
    回帰式がデータをどれだけうまく説明できているかを表す指標。

    計算式：R² = 1 - (残差の二乗和 / 全変動の二乗和)
    - 残差の二乗和：実際の値と予測値のズレの2乗の合計（予測で説明できなかった分）
    - 全変動の二乗和：実際の値と平均値のズレの2乗の合計（データ全体のばらつき）

    特徴：
    - 0〜1の範囲を取り、1に近いほど当てはまりが良い
    - 例えば R² = 0.8 なら「yのばらつきの80%を回帰式で説明できている」という意味
    - 説明変数を増やすと（意味のない変数でも）R² は上がりやすい点に注意
    """
    residual_sum_of_squares = ((y_actual - y_predicted) ** 2).sum()
    total_sum_of_squares = ((y_actual - y_actual.mean()) ** 2).sum()
    return 1 - residual_sum_of_squares / total_sum_of_squares


# CSVを読み込む
# 列：name（名前）, study_hours（勉強時間h）, sleep_hours（睡眠時間h）, test_score（テストの点数）
# → 「勉強時間や睡眠時間から、テストの点数を予測できるか」を回帰分析で調べる
input_data = pd.read_csv('regression_data/regression_data.csv')

print('=== 元データ ===')
print(input_data)

# ------------------------------------------------------------
# 1. 単回帰分析：勉強時間 → テストの点数
# ------------------------------------------------------------
# 説明変数（原因側・予測に使う値）と目的変数（結果側・予測したい値）を取り出す
x_study = input_data['study_hours']
y_score = input_data['test_score']

slope, intercept = simple_linear_regression(x_study, y_score)

# 求めた回帰式を使って、各データの予測値を計算する
simple_predicted = slope * x_study + intercept
simple_r2 = r_squared(y_score, simple_predicted)

print('\n=== 単回帰分析（勉強時間 → 点数） ===')
print(f'回帰式：点数 = {slope:.3f} × 勉強時間 + {intercept:.3f}')
print(f'→ 勉強時間が1時間増えると、点数は約 {slope:.2f} 点上がる')
print(f'決定係数 R²：{simple_r2:.3f}')

# numpy の polyfit（多項式フィッティング）でも同じ結果になることを確認する
# deg=1 は「1次式（直線）」で近似するという意味
np_slope, np_intercept = np.polyfit(x_study, y_score, deg=1)
print(f'（確認）np.polyfit の結果：傾き = {np_slope:.3f}, 切片 = {np_intercept:.3f}')

# 求めた回帰式で、新しいデータの点数を予測してみる
# 注意：元データの範囲（1〜8時間）の外側を予測する「外挿」は信頼性が低い
# 例えば 9時間で計算すると100点を超えてしまうなど、現実にあり得ない値になることがある
new_study_hours = 5.25
print(f'予測：勉強時間 {new_study_hours} 時間 → 約 {slope * new_study_hours + intercept:.1f} 点')

# ------------------------------------------------------------
# 2. 重回帰分析：勉強時間 + 睡眠時間 → テストの点数
# ------------------------------------------------------------
feature_columns = ['study_hours', 'sleep_hours']
x_features = input_data[feature_columns]

coefficients = multiple_linear_regression(x_features, y_score)
b0, b_study, b_sleep = coefficients

# 予測値 = b0 + b1 * 勉強時間 + b2 * 睡眠時間
multiple_predicted = b0 + b_study * input_data['study_hours'] + b_sleep * input_data['sleep_hours']
multiple_r2 = r_squared(y_score, multiple_predicted)

print('\n=== 重回帰分析（勉強時間 + 睡眠時間 → 点数） ===')
print(f'回帰式：点数 = {b0:.3f} + {b_study:.3f} × 勉強時間 + {b_sleep:.3f} × 睡眠時間')
print(f'→ 睡眠時間が同じなら、勉強時間1時間で約 {b_study:.2f} 点上がる')
print(f'→ 勉強時間が同じなら、睡眠時間1時間で約 {b_sleep:.2f} 点上がる')
print(f'決定係数 R²：{multiple_r2:.3f}（単回帰：{simple_r2:.3f}）')

# 実際の値・予測値・残差（ズレ）を並べて比較する
comparison = pd.DataFrame({
    'name': input_data['name'],
    'actual': y_score,
    'simple_pred': simple_predicted.round(1),
    'multiple_pred': multiple_predicted.round(1),
    'multiple_residual': (y_score - multiple_predicted).round(1),
})
print('\n=== 実測値と予測値の比較 ===')
print(comparison)

# ------------------------------------------------------------
# 3. 可視化
# ------------------------------------------------------------
fig, axes = plt.subplots(1, 3, figsize=(16, 5))

# (1) 単回帰：散布図に回帰直線を重ねる
# 点が直線の近くに集まっているほど、当てはまりが良いことを表す
axes[0].scatter(x_study, y_score, color='navy', label='actual data')
line_x = np.linspace(x_study.min(), x_study.max(), 100)
axes[0].plot(line_x, slope * line_x + intercept, color='crimson',
             label=f'y = {slope:.2f}x + {intercept:.2f}')
axes[0].set_title(f'Simple Regression (R² = {simple_r2:.3f})')
axes[0].set_xlabel('study_hours')
axes[0].set_ylabel('test_score')
axes[0].legend()
axes[0].grid(True)

# (2) 重回帰：実測値 vs 予測値
# 説明変数が2つ以上だと直線では描けないため、
# 「実測値」と「予測値」を比較する。点が対角線（y = x）上に並ぶほど予測が正確
axes[1].scatter(y_score, multiple_predicted, color='seagreen', label='multiple regression')
axes[1].scatter(y_score, simple_predicted, color='gray', alpha=0.5, label='simple regression')
score_range = [y_score.min(), y_score.max()]
axes[1].plot(score_range, score_range, color='crimson', linestyle='--', label='perfect prediction')
axes[1].set_title(f'Actual vs Predicted (multiple R² = {multiple_r2:.3f})')
axes[1].set_xlabel('actual test_score')
axes[1].set_ylabel('predicted test_score')
axes[1].legend()
axes[1].grid(True)

# (3) 残差プロット：予測値ごとの「ズレ（実測値 - 予測値）」
# 残差が0の線の上下にランダムに散らばっていれば、回帰モデルが妥当と判断できる
# 逆に、曲線状などのパターンが見える場合は、直線のモデルが合っていない可能性がある
axes[2].scatter(multiple_predicted, y_score - multiple_predicted, color='darkorange')
axes[2].axhline(0, color='crimson', linestyle='--')
axes[2].set_title('Residual Plot (multiple regression)')
axes[2].set_xlabel('predicted test_score')
axes[2].set_ylabel('residual (actual - predicted)')
axes[2].grid(True)

plt.tight_layout()
plt.show()
