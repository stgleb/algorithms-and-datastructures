def search_kth_simple(a1, a2, k_req):
    i, j, k = 0, 0, 0
    while i < len(a1) and j < len(a2) and k < k_req:
        if a1[i] < a2[j]:
            if k + 1 == k_req:
                return a1[i]
            i += 1
            k += 1
        else:
            if k + 1 == k_req:
                return a2[j]
            j += 1
            k += 1

    while i < len(a1) and k < k_req:
        if k + 1 == k_req:
            return a1[i]
        i += 1
        k += 1

    while j < len(a1) and k < k_req:
        if k + 1 == k_req:
            return a2[j]
        j += 1
        k += 1


def search_kth(a1, a2, k):
    n = len(a1)
    m = len(a2)
    mid1 = n // 2
    mid2 = m // 2

    while mid1 + mid2 + 1 != k:
        if mid1 + mid2 + 1 < k:
            if a1[mid1] < a2[mid2]:
                a1 = a1[mid1:]
                k -= mid1 - 1
            else:
                a2 = a2[mid2:]
                k -= mid2 - 1
        else:
            if a1[mid1] > a2[mid2]:
                a1 = a1[:mid1]
            else:
                a2 = a2[:mid2]
        mid1 = len(a1) // 2
        mid2 = len(a2) // 2

    return min(a1[mid1], a2[mid2])


if __name__ == "__main__":
    a1 = [2, 3, 6, 7, 9]
    a2 = [1, 4, 8, 10]
    print(search_kth_simple(a1, a2, 6))
    print(search_kth(a1, a2, 6))
