def has_cycles(graph):
    stack = [0]
    n = len(graph)
    colors = [0 for _ in range(n)]
    colors[0] = 1
    while stack:
        cur = stack[-1]
        added = False
        for v, reachable in enumerate(graph[cur]):
            if reachable:
                if colors[v] == 1:
                    return True
                if colors[v] == 0:
                    colors[v] = 1
                    stack.append(v)
                    added = True

        if not added:
            colors[cur] = 2
            stack.pop()
    return False


if __name__ == "__main__":
    graph = [
        [0, 1, 1, 0],
        [0, 0, 0, 1],
        [0, 0, 0, 1],
        [0, 0, 0, 0],
    ]
    print(has_cycles(graph))
