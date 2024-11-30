import numpy as np

def inverse_matrix_manual(matrix):
    # 行列が正方行列であることを確認
    if matrix.shape[0] != matrix.shape[1]:
        raise ValueError("逆行列を求めるには正方行列である必要があります。")
    
    # 行列式を計算
    det = matrix[0, 0] * matrix[1, 1] - matrix[0, 1] * matrix[1, 0]
    if det == 0:
        raise ValueError("逆行列は存在しません。")
    
    # 余因子行列を計算
    n = matrix.shape[0]
    cofactor_matrix = np.zeros_like(matrix, dtype=float)
    for i in range(n):
        for j in range(n):
            # 小行列を計算
            minor = np.delete(np.delete(matrix, i, axis=0), j, axis=1)
            cofactor_matrix[i, j] = ((-1) ** (i + j)) * np.linalg.det(minor)
    
    # 随伴行列（余因子行列の転置）
    adjugate = cofactor_matrix.T
    
    # 逆行列を計算
    inverse = adjugate / det
    return inverse



if __name__ == '__main__':

    # サンプル行列
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
        print(matrix)
        print("\n逆行列:")
        print(result)
    except ValueError as e:
        print(e)
