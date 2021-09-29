def pascal_triangle(n):
    a = []
    for i in range(n):
        a.append([0 for _ in range(n - i)])
        for j in range(n - i):
            if i == 0 or j == 0:
                a[i][j] = 1
            else:
                a[i][j] = a[i - 1][j] + a[i][j - 1]
        print(a[i][:n - i])


if __name__ == "__main__":
    pascal_triangle(10)
