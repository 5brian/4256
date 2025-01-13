import numpy as np

def identity_np(n):
    return np.eye(n, dtype=int)

def identity(n):
    matrix = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        matrix[i][i] = 1

    return matrix

def every_other_column(m, n):
    matrix = [[0 for _ in range(n)] for _ in range(m)]

    count = 1

    for col in range(0, n, 2):
        for row in range(m):
            matrix[row][col] = count
            count +=1

    return matrix
