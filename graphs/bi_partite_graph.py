def is_bipartite(graph):
    n = len(graph)
    colors = [0 for _ in range(n)]
    q = [0]
    color = 1
    colors[0] = color
    while q:
        cur = q[0]
        q = q[1:]
        color = -color
        for i in range(n):
            if graph[cur][i]:
                if colors[i] == 0:
                    q.append(i)
                if colors[i] == colors[cur]:
                    return False
                colors[i] = color
    return True


if __name__ == "__main__":
    graph = [
        [0, 1, 0, 0],
        [0, 0, 1, 0],
        [0, 0, 0, 1],
        [1, 0, 1, 0],
    ]
    print(is_bipartite(graph))
