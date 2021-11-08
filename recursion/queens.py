def solve(row, n, columns_placement, result):
    if n == row:
        result.append(columns_placement.copy())
    for col in range(n):
        is_valid = True
        for r, c in enumerate(columns_placement[:row]):
            if abs(col - c) == row - r or col == c:
                is_valid = False
                break
        if is_valid:
            columns_placement[row] = col
            solve(row + 1, n, columns_placement, result)


def get_desk(placement, n):
    desk = []
    for i in range(n):
        row = []
        for _ in range(n):
            row.append("_")
        row[placement[i]] = "*"
        desk.append(row)
    return desk


if __name__ == "__main__":
    n = 8
    columns = [0 for _ in range(n)]
    result = []
    solve(0, n, columns, result)
    for r in result:
        desk = get_desk(r, n)
        for row in desk:
            print(row)
        print("------------------")

