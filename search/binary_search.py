def binary_search(a, val):
    l, r = 0, len(a)
    while l <= r:
        m = (l + r) // 2
        if a[m] == val:
            return m
        elif a[m] < val:
            l = m + 1
        else:
            r = m - 1
    return -1


if __name__ == "__main__":
    print(binary_search([1, 2, 3, 4, 5, 6, 7, 8], 6))
