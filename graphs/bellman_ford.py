def shortest_path(graph, start):
    n = len(graph)
    distances = [float('inf') for _ in range(n)]
    distances[start] = 0
    predecessor = [-1 for _ in range(n)]

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if graph[i][j] != 0 and graph[i][j] + distances[i] < distances[j]:
                    distances[j] = graph[i][j] + distances[i]
                    predecessor[j] = i
    return distances


if __name__ == "__main__":
    graph = [
        [0, 4, 0, 0, 0, 0, 0, 8, 0],
        [4, 0, 8, 0, 0, 0, 0, 11, 0],
        [0, 8, 0, 7, 0, 4, 0, 0, 2],
        [0, 0, 7, 0, 9, 14, 0, 0, 0],
        [0, 0, 0, 9, 0, 10, 0, 0, 0],
        [0, 0, 4, 14, 10, 0, 2, 0, 0],
        [0, 0, 0, 0, 0, 2, 0, 1, 6],
        [8, 11, 0, 0, 0, 0, 1, 0, 7],
        [0, 0, 2, 0, 0, 0, 6, 7, 0]
    ]
    print(shortest_path(graph, 0))
