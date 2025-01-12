# 1
def identity(n):
    matrix = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        matrix[i][i] = 1

    return matrix
