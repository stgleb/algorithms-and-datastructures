def longest_distinct_subarray(a):
    latest = {}
    longest = 0
    beg, end = 0, 0
    cur = 0
    for i in range(len(a)):
        if a[i] not in latest:
            latest[a[i]] = i
            cur += 1
        else:
            prev_index = latest[a[i]]
            if i - prev_index > longest:
                longest = i - prev_index
                beg = prev_index
                end = i
            cur = 0
    return a[beg:end]


if __name__ == "__main__":
    print(longest_distinct_subarray([2, 1, 3, 4, 5, 2, 6, 7, 1, 5, 8, 10]))
