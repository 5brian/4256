def transpose_d(di):
    result = {}

    for node in di:
        result[node] = []

    for node, edges in di.items():
        for dest in edges:
            if dest not in result:
                result[dest] = []
            result[dest].append(node)

    return result

# helper
def bfs(graph, start):
    visited = set([start])
    queue = [start]

    while queue:
        node = queue.pop(0)
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return visited

def weakly_connected(di):
    if not di:
        return True

    undirected = {}
    for node in di:
        if node not in undirected:
            undirected[node] = []
        for neighbor in di[node]:
            if neighbor not in undirected:
                undirected[neighbor] = []
            if neighbor not in undirected[node]:
                undirected[node].append(neighbor)
            if node not in undirected[neighbor]:
                undirected[neighbor].append(node)

    start_node = next(iter(undirected))
    visited = bfs(undirected, start_node)

    return len(visited) == len(undirected)

def greatest_weight_d(di):
    max_weight = float('-inf')
    source_node = None
    dest_node = None

    for source, destinations in di.items():
        for dest, weight in destinations.items():
            if weight > max_weight:
                max_weight = weight
                source_node = source
                dest_node = dest

    return (max_weight, source_node, dest_node)

def incidence_to_matrix(inc):
    num_vertices = len(inc)
    adj_matrix = [[0 for _ in range(num_vertices)] for _ in range(num_vertices)]

    if not inc or not inc[0]:
        return adj_matrix

    num_edges = len(inc[0])

    for e in range(num_edges):
        vertices = []
        for v in range(num_vertices):
            if inc[v][e] == 1:
                vertices.append(v)

        if len(vertices) == 2:
            v1, v2 = vertices
            adj_matrix[v1][v2] = 1
            adj_matrix[v2][v1] = 1

    return adj_matrix

def dict_to_incidence(graph_dict):
    vertices = list(graph_dict.keys())

    edges = []
    for u in vertices:
        for v in graph_dict[u]:
            if not ((u, v) in edges or (v, u) in edges):
                edges.append((u, v))

    incidence_matrix = [[0 for _ in range(len(edges))] for _ in range(len(vertices))]

    for edge_idx, (u, v) in enumerate(edges):
        u_idx = vertices.index(u)
        v_idx = vertices.index(v)

        incidence_matrix[u_idx][edge_idx] = 1
        incidence_matrix[v_idx][edge_idx] = 1

    return (vertices, edges, incidence_matrix)
