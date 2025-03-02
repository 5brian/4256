'''
Write a function called directed to undirected(di) that takes a matrix
representation of a directed graph as an argument and returns a matrix repre-
sentation of its underlying undirected graph.
For example, if di =
[[0, 1, 1, 0, 0],
[0, 0, 0, 0, 0],
[0, 0, 0, 0, 1],
[1, 1, 0, 0, 1],
[0, 0, 0, 0, 0]]
the function should return
[[0, 1, 1, 1, 0],
[1, 0, 0, 1, 0],
[1, 0, 0, 0, 1],
[1, 1, 0, 0, 1],
[0, 0, 1, 1, 0]]
'''
def directed_to_undirected(di):
    n = len(di)
    undirected = [row[:] for row in di]

    for i in range(n):
        for j in range(n):
             if di[i][j] == 1 or di[j][i] == 1 :
                undirected[i][j] = 1
                undirected[j][i] = 1

    return undirected
