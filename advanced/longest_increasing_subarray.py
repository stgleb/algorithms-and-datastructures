def longest_increasing_subarray(a):
    i = 0
    max_len = 0
    start, end = 0, 0
    n = len(a)
    while i < n:
        j = i
        while j < n - 1 and a[j] < a[j + 1]:
            j += 1
        if j - i > max_len:
            max_len = j - 1
            start = i
            end = j + 1
        i = j + 1

    return a[start:end]


if __name__ == "__main__":
    print(longest_increasing_subarray([2, 1, -1, 5, 4, 6, 7, 10, 1, 2, 3]))
