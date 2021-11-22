def find_missing(a):
    i = 0
    j = 0
    while i < len(a):
        if a[i] >= 0:
            a[a[i]], a[i] = a[i], a[a[i]]
            j += 1
        i += 1
    for i in range(j):
        if a[i] < 0:
            return i
    return j


if __name__ == "__main__":
    a = [-1, 2, 1, -4, 0, 5, 3, -2]
    print(find_missing(a))
