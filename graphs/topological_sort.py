def topological_sort(graph):
    n = len(graph)
    stack = []
    visited = [False for _ in range(n)]

    def dfs(graph, cur):
        visited[cur] = True
        for v in range(n):
            if graph[cur][v] != 0 and not visited[v]:
                dfs(graph, v)
        stack.append(cur)

    for i in range(n):
        if not visited[i]:
            dfs(graph, i)
    return stack[::-1]


if __name__ == "__main__":
    graph = [
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [1, 1, 0, 0, 0, 0],
        [1, 0, 1, 0, 0, 0],
    ]
    print(topological_sort(graph))
