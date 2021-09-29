
def rotate(a, n):
    for i in range(n // 2):
        for j in range(i, n - i - 1):
            a[i][j], a[j][n - i - 1], a[n - i - 1][n - j - 1], a[n - j - 1][i] = \
                a[n - j - 1][i], a[i][j], a[j][n - i - 1], a[n - i - 1][n - j - 1]

    return a


if __name__ == "__main__":
    n = 3
    matrix = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n * n):
        matrix[i // n][i % n] = i

    for i in range(n):
        print(matrix[i])

    rotate(matrix, n)
    for i in range(n):
        print(matrix[i])
    print("---------------------")
    n = 4
    matrix = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n * n):
        matrix[i // n][i % n] = i

    for i in range(n):
        print(matrix[i])

    rotate(matrix, n)
    for i in range(n):
        print(matrix[i])
    print("---------------------")
    n = 5
    matrix = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n * n):
        matrix[i // n][i % n] = i

    for i in range(n):
        print(matrix[i])
    rotate(matrix, n)

    for i in range(n):
        print(matrix[i])
