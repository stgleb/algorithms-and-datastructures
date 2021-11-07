from heapq import heappop as pop
from heapq import heappush as push


def shortest_covering_interval(a1, a2, a3):
    heap = []
    push(heap, (a1[0], 0, a1))
    push(heap, (a2[0], 0, a2))
    push(heap, (a3[0], 0, a3))
    rolling_max = max(a1[0], a2[0], a3[0])
    min_interval_len = 1000
    min_start, min_end = -1, -1
    while heap:
        val, index, a = pop(heap)
        if rolling_max - val < min_interval_len:
            min_interval_len = rolling_max - val
            min_start = val
            min_end = rolling_max
        if index + 1 == len(a):
            break
        new_val = a[index + 1]
        push(heap, (new_val, index + 1, a))
        rolling_max = max(new_val, rolling_max)
        
    return min_interval_len, min_start, min_end


if __name__ == "__main__":
    print(shortest_covering_interval([1, 3, 4, 5, 7], [3, 6, 8, 9, 10, 15], [8, 9, 16, 24]))
