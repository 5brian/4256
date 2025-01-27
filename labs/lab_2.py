import numpy as np

# 1a
def anti_diag(n):
    matrix = []

    for i in range(n):
        row = [0] * n
        row[n - 1 - i] = 1
        matrix.append(row)

    return matrix

# print(anti_diag(5))

# 1b
def anti_diag_2(n):
    return(np.fliplr(np.identity(n)))

# print(anti_diag_2(5))

# 1c
def anti_diag_3(n):
    return(np.rot90(np.identity(n)))

# print(anti_diag_3(5))

# 1d
def anti_diag_4(n):
    return(np.flipud(np.identity(n)))

# print(anti_diag_4(5))

# 2
def border(m,n):
    return

# print(border(3,4))

# 3a
def transpose(mat):
    transposed = []

    for j in range(len(mat[0])):
        new_row = []
        for i in range(len(mat)):
            new_row.append(mat[i][j])
        transposed.append(new_row)

    return transposed

# print(transpose([[2, -1, 5, 6],[0, 9, 12, -4],[-3, -2, 9, 1]]))

# 3b
def transpose_2(mat):
    return np.transpose(mat)

# print(transpose_2([[2, -1, 5, 6],[0, 9, 12, -4],[-3, -2, 9, 1]]))

# 4a
def dot_product(l1,l2):
    zipped = zip(l1,l2)
    return sum([i[0]*i[1] for i in zipped])

# print(dot_product([2,-2,4],[5,1,2]))

# 4b
def dot_product_2(l1,l2):
    return(np.dot(l1,l2))

# print(dot_product_2([2,-2,4],[5,1,2]))

# 5a
def is_u_t(mat):
    for i in range(len(mat)):
        for j in range(i+1,len(mat)):
            if mat[i][j] != 0:
                return False
    return True

# print(is_u_t([[[1, -3, 3, 4], [0, 0, 2, 0], [0, 0, 3, -2], [0, 0, 0, 3]]]))

# 5b
def is_u_t_n(mat):
    return(np.array_equal(mat,np.triu(mat)))

# print(is_u_t_n([[[1, -3, 3, 4], [0, 0, 2, 0], [0, 0, 3, -2], [0, 0, 0, 3]]]))

# 6
def chessboard(n):
    mat = [[0 for i in range(n)] for j in range(n)]
    for i in range(n):
        for j in range(n):
            if (i+j)%2 == 0:
                mat[i][j]=1
    return mat

# print(chessboard(5))
# print(chessboard(6))

# 7
def is_toeplitz(mat):
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            if i>0 and j>0:
                if mat[i][j] != mat[i-1][j-1]:
                    return False
    return True

# print(is_toeplitz([[1, 3, 4], [2, 1, 3], [3, 2, 1], [4, 3, 2]]))
