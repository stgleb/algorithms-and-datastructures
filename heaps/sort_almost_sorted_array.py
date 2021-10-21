from heapq import  heappush as push
from heapq import heappop as pop


def sort_almost_sorted(a, k):
    h = []
    result = []

    for i in range(k):
        push(h, a[i])

    for i in range(k, len(a)):
        result.append(pop(h))
        push(h, a[i])

    while h:
        result.append(pop(h))

    return result


if __name__ == "__main__":
    print(sort_almost_sorted([1, 2, 5, 4, 3, 6, 7, 9, 8, 10],  3))
