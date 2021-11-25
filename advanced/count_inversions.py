def merge_sort(a, tmp, l, m, r):
    i = l
    j = m + 1
    k = l
    inv_count = 0
    while i <= m and j <= r:
        if a[i] < a[j]:
            tmp[k] = a[i]
            i += 1
            k += 1
        else:
            tmp[k] = a[j]
            j += 1
            k += 1
            inv_count += (m - i) + 1
    while i <= m:
        tmp[k] = a[i]
        k += 1
        i += 1
    while j <= r:
        tmp[k] = a[j]
        k += 1
        j += 1
    for i in range(l, r):
        a[i] = tmp[i]

    return inv_count


def merge_util(a, tmp, l, r):
    inv_count = 0
    mid = (l + r) // 2

    if l < r:
        inv_count += merge_util(a, tmp, l, mid)
        inv_count += merge_util(a, tmp, mid + 1, r)
        inv_count += merge_sort(a, tmp, l, mid, r)
    return inv_count


def merge(a):
    tmp = [0] * len(a)
    return merge_util(a, tmp, 0, len(a) - 1)


if __name__ == "__main__":
    a = [1, 20, 6, 4, 5]
    print(merge(a))
