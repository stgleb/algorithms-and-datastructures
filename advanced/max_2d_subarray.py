def max_subarray(a):
    max_sum = 0
    current_sum = 0
    start = 0
    end = 0
    max_start = 0
    max_end = 0
    for i in range(len(a)):
        current_sum += a[i]
        end = i
        if current_sum < 0:
            current_sum = 0
            start = i + 1
        elif max_sum < current_sum:
            max_sum = current_sum
            max_start = start
            max_end = end
    return max_sum, max_start, max_end


def max_subarray_2d(a):
    n = len(a)
    m = len(a[0])
    accum_sum = [[0] * m for _ in range(n)]
    for j in range(m):
        for i in range(n):
            if i == 0:
                accum_sum[i][j] = a[i][j]
            else:
                accum_sum[i][j] = accum_sum[i - 1][j] + a[i][j]

    max_sum = 0
    max_start, max_end = 0, 0
    max_i = 0
    max_j = 0
    for i in range(n):
        for j in range(i, n):
            tmp_sum = [0] * m

            for k in range(m):
                tmp_sum[k] = accum_sum[j][k] - accum_sum[i][k]

            tmp_sum, start, end = max_subarray(tmp_sum)
            if max_sum < tmp_sum:
                max_sum = tmp_sum
                max_start = start
                max_end = end
                max_i = i + 1
                max_j = j

    return max_sum, max_start, max_end, max_i, max_j


if __name__ == "__main__":
    a = [[1, 2, -1, -4, -20],
         [-8, -3, 4, 2, 1],
         [3, 8, 10, 1, 3],
         [-4, -1, 1, 7, -6]]
    print(max_subarray_2d(a))

