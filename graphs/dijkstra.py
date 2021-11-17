from heapq import heappush as push
from heapq import heappop as pop


def shortest_path(graph, start):
    q = [(0, start)]
    n = len(graph)
    distances = [float('inf') for _ in range(n)]
    distances[start] = 0
    prev = [-1 for _ in range(n)]
    visited = [False for _ in range(n)]
    visited[start] = True
    while q:
        distance, cur = pop(q)
        for v, d in enumerate(graph[cur]):
            if d != 0 and distances[v] > distances[cur] + d:
                distances[v] = distances[cur] + d
                prev[v] = cur
                push(q, (distances[v], v))
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
