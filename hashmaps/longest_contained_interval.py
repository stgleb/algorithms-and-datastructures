def longest_contained_interval(a):
    intervals = {}
    for i in range(len(a)):
        if a[i] not in intervals:
            intervals[a[i]] = 1

    for key in intervals:
        if key - 1 in intervals:
            intervals[key] += intervals[key - 1]
        if key + 1 in intervals:
            intervals[key] += intervals[key + 1]

    max_key, max_val = 0, 0

    for key, val in intervals.items():
        if val > max_val:
            max_key = key
            max_val = val

    result = []
    i = 0
    while max_key - i in intervals:
        result.append(max_key - i)
        i += 1

    i = 0
    while max_key + i in intervals:
        result.append(max_key + i)
        i += 1
    return sorted(set(result))


if __name__ == "__main__":
    print(longest_contained_interval([3, -2, 7, 9, 8, 1, 2, 0, -1, 5, 8]))
