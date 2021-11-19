def articulation_points_util(graph, u, visited, disc, low, parent, time, result):
    time[0] += 1
    visited[u] = True
    disc[u] = time[0]
    low[u] = time[0]
    children = 0
    for v in graph[u]:
        if v != 0:
            children += 1
    for v, _ in enumerate(graph[u]):
        if not visited[v]:
            parent[v] = u
            articulation_points_util(graph, v, visited, disc, low, parent, time, result)
            low[u] = min(low[u], low[v])
            if parent[u] == -1 and children > 1:
                result.append(u)
            if parent[u] != -1 and low[v] > disc[u]:
                result.append(u)
        elif v != parent[u]:
            low[u] = min(low[u], disc[v])


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
        [0, 1, 1, 0, 0, 0, 0],
        [1, 0, 1, 0, 1, 0, 1],
        [1, 1, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 1, 0],
        [0, 1, 0, 0, 0, 1, 0],
        [0, 0, 0, 1, 1, 0, 0],
        [0, 1, 0, 0, 0, 0, 0],
    ]
    print(articulation_points(graph))
