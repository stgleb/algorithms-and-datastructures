def number_of_traversal(n, m):
    ways = [[0 for _ in range(m)] for _ in range(n)]
    for i in range(n):
        ways[i][0] = 1
    for i in range(m):
        ways[0][i] = 1

    for i in range(1, n):
        for j in range(1, m):
            ways[i][j] = ways[i - 1][j] + ways[i][j - 1]
    return ways[n - 1][m - 1]


if __name__ == "__main__":
    print(number_of_traversal(3, 4))

