def bridges_util(graph, u, visited, disc, low, parent, time, result):
    visited[u] = True
    disc[u] = time[0]
    low[u] = time[0]
    time[0] += 1

    for v, w in enumerate(graph[u]):
        if w:
            if parent[v] == u:
                continue
            elif visited[v]:
                low[u] = min(low[u], disc[v])
            else:
                parent[v] = u
                bridges_util(graph, v, visited, disc, low, parent, time, result)
                low[u] = min(low[u], low[v])
                if low[v] >= disc[u]:
                    result.append((u, v))


def bridges(graph):
    n = len(graph)
    result = []
    disc = [float('inf') for _ in range(n)]
    low = [float('inf') for _ in range(n)]
    parent = [-1 for _ in range(n)]
    visited = [False for _ in range(n)]
    time = [0]
    for i in range(n):
        if not visited[i]:
            bridges_util(graph, i, visited, disc, low, parent, time, result)
    return result


if __name__ == "__main__":
    graph = [
        [0, 1, 0, 0],
        [1, 0, 1, 0],
        [0, 1, 0, 1],
        [0, 0, 1, 0],
    ]
    print(bridges(graph))
