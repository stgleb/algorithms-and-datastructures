def find_k_largest(a, k):
    l, r = -1, 0
    pivot = a[len(a) // 2]
    while r < len(a):
        if a[r] < pivot:
            l += 1
            a[l], a[r] = a[r], a[l]
        r += 1

    if r - l - 1 == k:
        return pivot
    elif r - l - 1 > k:
        return find_k_largest(a[l + 1:], k)
    else:
        return find_k_largest(a[:l + 1], k - (r - l - 1))


if __name__ == "__main__":
    print(find_k_largest([2, 1, 3, 4, 10, 11, 5, 8, 9, 7], 4))
