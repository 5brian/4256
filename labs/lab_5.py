def cycle_m(n):
    if n <= 2:
        return None

    matrix = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        matrix[i][(i + 1) % n] = 1
        matrix[i][(i - 1) % n] = 1

    return matrix

def cycle_d(n):
    if n <= 2:
        return None

    graph = {}
    for i in range(n):
        graph[i] = {(i + 1) % n, (i - 1) % n}

    return graph

def is_regular_m(mat):
    if not mat or not mat[0]:
        return False

    first_degree = sum(mat[0])

    for row in mat:
        if sum(row) != first_degree:
            return False

    return True

def is_regular_d(di):
    if not di:
        return False

    first_degree = len(di[0])

    for vertex in di:
        if len(di[vertex]) != first_degree:
            return False

    return True

def complete_bipartite_d(m, n):
    if m <= 0 or n <= 0:
        return None

    graph = {}

    for i in range(m):
        graph[i] = set(range(m, m + n))

    for i in range(m, m + n):
        graph[i] = set(range(m))

    return graph

def complete_bipartite_m(m, n):
    if m <= 0 or n <= 0:
        return None

    size = m + n
    matrix = [[0 for _ in range(size)] for _ in range(size)]

    for i in range(m):
        for j in range(m, m + n):
            matrix[i][j] = 1
            matrix[j][i] = 1

    return matrix

def di_to_mat(di):
    n = max(max(di.keys()), max(v for s in di.values() for v in s)) + 1

    matrix = [[0 for _ in range(n)] for _ in range(n)]

    for vertex in di:
        for neighbor in di[vertex]:
            matrix[vertex][neighbor] = 1

    return matrix

def bfs_m(mat, start_node=0):
    n = len(mat)
    distances = [-1] * n
    distances[start_node] = 0

    queue = [start_node]
    visited = {start_node}

    while queue:
        current = queue.pop(0)

        for neighbor in range(n):
            if mat[current][neighbor] == 1 and neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
                distances[neighbor] = distances[current] + 1

    return distances
