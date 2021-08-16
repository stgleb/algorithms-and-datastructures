# Given array of elements 0,1 and 2
# sort that array in O(N) time and O(1) memory.

def dutch_sort(a):
    l, i, r = 0, 0, len(a) - 1
    while i <= r:
        if a[i] == 0:
            a[i], a[l] = a[l], a[i]
            l += 1
            i += 1
        elif a[i] == 2:
            a[i], a[r] = a[r], a[i]
            r -= 1
        elif a[i] == 1:
            i += 1
    return a


if __name__ == "__main__":
    print(dutch_sort([1, 2, 0, 1, 1, 0, 2, 0, 1]))
