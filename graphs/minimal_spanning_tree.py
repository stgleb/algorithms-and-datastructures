def minimal_spanning_tree(graph):
    n = len(graph)
    edges = []
    for i in range(n):
        for j in range(i, n):
            if graph[i][j]:
                edges.append((graph[i][j], i, j))
    v = [-1 for _ in range(n)]
    component_count = 0
    mst_edges = []
    for e, i, j in sorted(edges):
        if v[i] == -1 and v[j] == -1:
            v[i] = component_count
            v[j] = component_count
            component_count += 1
        elif v[i] == -1 or v[j] == -1:
            v[i] = max(v[i], v[j])
            v[j] = max(v[i], v[j])
        elif v[i] != v[j]:
            min_comp, max_comp = min(v[i], v[j]), max(v[i], v[j])
            for k in range(n):
                if v[k] == max_comp:
                    v[k] = min_comp
        else:
            continue
        mst_edges.append((e, i, j))

    mst = [[0 for _ in range(n)] for _ in range(n)]
    for e, i, j in mst_edges:
        mst[i][j] = e
    return mst


if __name__ == "__main__":
    graph = [
        [0, 2, 0, 6, 0],
        [2, 0, 3, 8, 5],
        [0, 3, 0, 0, 7],
        [6, 8, 0, 0, 9],
        [0, 5, 7, 9, 0],
    ]
    print(minimal_spanning_tree(graph))
