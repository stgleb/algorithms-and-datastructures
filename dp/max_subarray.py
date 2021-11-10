def max_subarray(a):
    start_index, end_index = 0, 0
    max_sum = 0
    rolling_sum = 0
    current_end = 0
    for i in range(len(a)):
        rolling_sum += a[i]
        if rolling_sum <= 0:
            current_end = i + 1
            rolling_sum = 0
        elif rolling_sum > max_sum:
            max_sum = rolling_sum
            start_index = current_end
            end_index = i
    return max_sum, a[start_index: end_index + 1]


if __name__ == "__main__":
    print(max_subarray([1, -3, -4, -5, -6, -3, -2, -7, -8, -4]))

