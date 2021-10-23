def search_index_value(a):
    l, r = 0, len(a)
    while l <= r:
        m = (l + r) // 2
        if a[m] == m:
            return m
        elif a[m] < m:
            l = m + 1
        else:
            r = m - 1
    return - 1


if __name__ == "__main__":
    print(search_index_value([1, 2, 2, 3, 3, 4, 6, 8, 9, 10]))
