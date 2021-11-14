from heapq import heappop as pop
from heapq import heappush as push


def trap_water(heights):
    n = len(heights)
    m = len(heights[0])
    visited = [[False for _ in range(m)] for _ in range(n)]
    h = []
    for i in range(n):
        push(h, (heights[i][0], i, 0))
        push(h, (heights[i][m - 1], i, m - 1))
        visited[i][0] = True
        visited[i][m - 1] = True

    for j in range(m):
        push(h, (heights[0][j], 0, j))
        push(h, (heights[n - 1][j], n - 1, j))
        visited[0][j] = True
        visited[n - 1][j] = True

    total = 0
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    cur_max = 0
    while h:
        height, i, j = pop(h)
        cur_max = max(height, cur_max)
        for dx, dy in directions:
            if i + dx > 0 and i + dx < n - 1 and j + dy > 0 and j + dy < m - 1 and \
                not visited[i + dx][j + dy]:
                if heights[i + dx][j + dy] < cur_max:
                    total += cur_max - heights[i + dx][j + dy]
                push(h, (heights[i + dx][j + dy], i + dx, j + dy))
                visited[i + dx][j + dy] = True

    return total


if __name__ == "__main__":
    heights = [
        [12, 13, 1, 12],
        [13, 4, 13, 12],
        [13, 8, 10, 12],
        [12, 13, 12, 12],
        [13, 13, 13, 13]
    ]
    print(trap_water(heights))
