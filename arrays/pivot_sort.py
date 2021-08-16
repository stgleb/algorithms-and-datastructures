# Given an array and pivot element index, sort
# that array around pivot element so elements bigger than
# that appears after and smaller that pivot appears before.
def pivot_sort(a, index):
    pivot = a[index]
    head, tail = -1, 0
    while tail < len(a):
        if a[tail] <= pivot:
            head += 1
            a[tail], a[head] = a[head], a[tail]
        tail += 1
    return a


if __name__ == "__main__":
    print(pivot_sort([2, 4, 1, 5, 0, 6, 3], 0))

