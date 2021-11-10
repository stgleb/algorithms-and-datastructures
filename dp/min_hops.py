import sys


def min_hops(hops):
    result = [sys.maxsize for _ in hops]
    result[0] = 0
    for i in range(len(hops)):
        hop = hops[i]
        for j in range(1, hop + 1):
            if i + j < len(hops):
                result[i + j] = min(result[i + j], result[i] + 1)
    return result[-1]


if __name__ == "__main__":
    print(min_hops([1, 3, 6, 3, 2, 3, 6, 8, 9, 5]))
