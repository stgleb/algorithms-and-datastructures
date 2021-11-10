def longest_increasing_subsequence(a):
    seq = [1 for _ in range(len(a))]
    restore = [-1 for _ in range(len(a))]

    for i in range(1, len(a)):
        j = i - 1
        while j >= 0:
            if a[j] < a[i]:
                if seq[i] < seq[j] + 1:
                    seq[i] = seq[j] + 1
                    restore[i] = j
            j -= 1
    index_max = len(a) - 1
    for i in range(len(a)):
        if seq[i] > seq[index_max]:
            index_max = i
    i = index_max
    while i >= 0:
        print(a[i])
        i = restore[i]
    return seq[index_max]


if __name__ == "__main__":
    print(longest_increasing_subsequence([10, 3, 2, 4, 6, 5, 7, 8, 0]))
