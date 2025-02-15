def star_m(n):
    if n<= 2:
        assert n > 2, "n must be greater than 2"


    matrix = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(1, n):
        matrix[0][i] = 1
        matrix[i][0] = 1

    return matrix

def star_d(n):
    if n < 2:
        assert n > 2, "n must be greater than 2"

    graph = {
        i: set() for i in range(n)
    }

    graph[0] = set(range(1,n))

    for i in range(1,n):
        graph[i] = {0}

    return graph
