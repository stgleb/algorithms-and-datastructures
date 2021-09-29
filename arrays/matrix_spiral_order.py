def cirlce(a, n, offset):
    result = []
    # we have odd dimension and we are at the center
    if offset == n - offset - 1:
        result.append(a[offset][offset])
        return result

    # move right
    for i in range(n - offset * 2):
        result.append(a[offset][offset + i])
    # move down
    for i in range(n - offset * 2 - 1):
        result.append(a[offset + i + 1][n - offset - 1])

    # move left
    for i in range(n - offset * 2 - 1):
        result.append(a[n - offset - 1][n - offset - 2 - i])
    # move up
    for i in range(n - offset * 2 - 2):
        result.append(a[n - offset - 2 - i][offset])
    return result


def spiral_order(a, n):
    result = []
    for i in range(n // 2 + 1):
        result += cirlce(a, n, i)
    print(result)


if __name__ == "__main__":
    n = 3
    matrix = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n * n):
        matrix[i // n][i % n] = i

    for i in range(n):
        print(matrix[i])

    spiral_order(matrix, n)
    print("---------------------")
    n = 4
    matrix = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n * n):
        matrix[i // n][i % n] = i

    for i in range(n):
        print(matrix[i])

    spiral_order(matrix, n)
    print("---------------------")
    n = 5
    matrix = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n * n):
        matrix[i // n][i % n] = i

    for i in range(n):
        print(matrix[i])
    spiral_order(matrix, n)