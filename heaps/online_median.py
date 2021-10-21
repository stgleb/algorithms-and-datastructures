from heapq import heappop as pop
from heapq import heappush as push


def online_median(stream):
    min_heap = []
    max_heap = []
    medians = []
    for val in stream:
        push(min_heap, val)
        while len(min_heap) > len(max_heap) + 1:
            val = pop(min_heap)
            push(max_heap, -val)

        medians.append(min_heap[0])

    return medians


if __name__ == "__main__":
    print(online_median([1, 2, 3, 4, 5, 5, 5, 8, 9, 10]))
