from fractions import Fraction
import numpy as np

# 逆行列算出力
def inverse_matrix_manual(matrix):
    # 行列が正方行列であることを確認
    if matrix.shape[0] != matrix.shape[1]:
        raise ValueError("逆行列を求めるには正方行列である必要があります。")
    
    # 行列式を計算
    det = matrix[0, 0] * matrix[1, 1] - matrix[0, 1] * matrix[1, 0]
    if det == 0:
        raise ValueError("逆行列は存在しません。")
       
    # 逆行列配列：float型で0埋め正方配列を作成
    cofactor_matrix = np.zeros_like(matrix, dtype=float)
    
    # 逆行列配列に値を配置
    cofactor_matrix[0][0] = matrix[1][1]
    cofactor_matrix[0][1] = -1 * matrix[0][1]
    cofactor_matrix[1][0] = -1 * matrix[1][0]
    cofactor_matrix[1][1] = matrix[0][0]
        
    # 逆行列を計算
    inverse = cofactor_matrix / det

    return inverse


# メイン処理
if __name__ == '__main__':

    # 問題の行列
    matrix_1 = np.array([[2, 6], [1, 3]])
    matrix_2 = np.array([[-3, 4], [2, -3]])
    matrix_3 = np.array([[5, 2], [1, 0]])
    matrix_4 = np.arange(8).reshape(2,4)

    matrix_list = [
        matrix_1
        , matrix_2
        , matrix_3
        , matrix_4
    ]

for matrix in matrix_list:
    print("-------------------------------")
    try:
        result = inverse_matrix_manual(matrix)
        print("元の行列:")
        # 少数の場合は分数表記
        print(np.vectorize(lambda x: str(Fraction(x).limit_denominator()))(matrix))
        print("\n逆行列:")
        # 少数の場合は分数表記
        print(np.vectorize(lambda x: str(Fraction(x).limit_denominator()))(result))
    except ValueError as e:
        print(e)
