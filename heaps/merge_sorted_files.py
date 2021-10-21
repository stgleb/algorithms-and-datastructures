import itertools
from heapq import heappush
from heapq import heappop


def merge(files):
    h = []
    result = []
    for i in range(len(files)):
        if len(files[i]):
            heappush(h, (files[i][0], i, 0))

    while h:
        val, file_index, offset = heappop(h)
        if offset > len(files[file_index]):
            continue
        result.append(val)
        if offset + 1 < len(files[file_index]):
            heappush(h, (files[file_index][offset + 1], file_index, offset + 1))

    return result


if __name__ == "__main__":
    files = [
        [7, 11, 17],
        [1, 2, 3, 4, 5],
        [-2, 18, 39, 40, 50, 60, 101],
        [1, 3, 5, 7, 9, 11, 19]
    ]
    print(merge(files))
