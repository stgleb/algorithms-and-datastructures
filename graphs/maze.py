def bfs(start_i, start_j, matrix):
    n = len(matrix)
    m = len(matrix[0])
    path_len = [[n * m for _ in range(m)] for _ in range(n)]
    path_len[start_i][start_j] = 0
    q = [(start_i, start_j, 0)]
    directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
    while q:
        i, j, l = q[0]
        q = q[1:]
        for dx, dy in directions:
            if i + dx >= 0 and i + dx < n and j + dy >= 0 and j + dy < m and path_len[i + dx][j + dy] > l + 1:
                path_len[i + dx][j + dy] = l + 1
                q.append((i + dx, j + dy, l + 1))
    return path_len


def dfs(start_i, start_j, matrix):
    n = len(matrix)
    m = len(matrix[0])
    path_len = [[n * m for _ in range(m)] for _ in range(n)]
    path_len[start_i][start_j] = 0
    stack = [(start_i, start_j, 0)]
    directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
    while stack:
        i, j, l = stack.pop()
        for dx, dy in directions:
            if i + dx >= 0 and i + dx < n and j + dy >= 0 and j + dy < m and path_len[i + dx][j + dy] > l + 1:
                path_len[i + dx][j + dy] = l + 1
                stack.append((i + dx, j + dy, l + 1))
    return path_len


if __name__ == "__main__":
    maze = [
        [1, 1, 1, 1, 1],
        [1, 0, 1, 0, 1],
        [1, 0, 1, 0, 1],
        [1, 1, 1, 1, 1],
        [1, 0, 0, 0, 1]
    ]
    print(bfs(0, 0, maze))
    print(dfs(0, 0, maze))
