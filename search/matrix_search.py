def matrix_search(matrix, val):
    row, col = 0, len(matrix[0]) - 1
    while row < len(matrix) and col >= 0:
        if matrix[row][col] == val:
            return (row, col)
        elif matrix[row][col] > val:
            col -= 1
        else:
            row += 1

    return -1 , -1


if __name__ == "__main__":
    matrix = [
        [1, 2, 3, 4, 5, 6, 7],
        [2, 3, 4, 5, 6, 7, 8],
        [5, 6, 7, 7, 7, 8, 9],
        [6, 6, 6, 7, 8, 17, 20],
        [10, 11, 12, 13, 18, 21]
    ]
    print(matrix_search(matrix, 12))

