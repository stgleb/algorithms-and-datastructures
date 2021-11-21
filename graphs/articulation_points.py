def articulation_points_util(graph, u, visited, disc, low, parent, time, result):
    visited[u] = True
    disc[u] = time[0]
    low[u] = time[0]
    time[0] += 1
    children = 0
    for v, w in enumerate(graph[u]):
        if w:
            if v == parent[u]:
                continue
            elif visited[v]:
                low[u] = min(low[u], disc[v])
            else:
                children += 1
                parent[v] = u
                articulation_points_util(graph, v, visited, disc, low, parent, time, result)
                low[u] = min(low[u], low[v])
                if parent[u] != -1 and low[v] >= disc[u]:
                    result.append(u)
    if parent[u] == -1 and children > 1:
        result.append(u)


def articulation_points(graph):
    n = len(graph)
    result = []
    visited = [False for _ in range(n)]
    parent = [-1 for _ in range(n)]
    disc = [float('inf') for _ in range(n)]
    low = [float('inf') for _ in range(n)]
    time = [0]
    for i in range(n):
        articulation_points_util(graph, i, visited, disc, low, parent, time, result)
    return result


if __name__ == "__main__":
    graph = [
        [0, 1, 1, 0, 0],
        [1, 0, 1, 0, 0],
        [1, 1, 0, 1, 1],
        [0, 0, 1, 0, 1],
        [0, 0, 1, 1, 0],
    ]
    print(articulation_points(graph))
