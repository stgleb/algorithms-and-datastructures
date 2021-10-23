def find_left_iter(a, val):
    l, r = 0, len(a)
    index = -1
    while l <= r:
        m = (l + r) // 2
        if a[m] == val:
            index = m
            break
        elif a[m] < val:
            l = m + 1
        else:
            r = m - 1

    while index > 0 and a[index - 1] == val:
        index -= 1

    return index


def find_left_binary(a, val):
    l, r = 0, len(a)
    index = - 1
    while l <= r:
        m = (l + r) // 2
        if a[m] == val:
            index = m
            r = m - 1
        elif a[m] < val:
            l = m + 1
        else:
            r = m - 1

    return index


if __name__ == "__main__":
    print(find_left_iter([1, 2, 2, 3, 3, 4, 5, 5, 5, 6, 7, 8], 5))
    print(find_left_binary([1, 2, 2, 3, 3, 4, 5, 5, 5, 6, 7, 8], 5))
