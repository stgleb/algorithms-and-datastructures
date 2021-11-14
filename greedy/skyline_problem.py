def skyline(buildings):
    points = []
    for start, end, height in buildings:
        points.append((start, True, height))
        points.append((end, False, height))
    points.sort()
    heap = []
    result = []
    cur_max = 0
    for p, status, height in points:
        if status:
            if cur_max < height:
                cur_max = height
                result.append((p, height))
            heap.append((p, height))
        else:
            for i in range(len(heap)):
                if heap[i][1] == height:
                    heap = heap[:i] + heap[i + 1:]
                    break
            cur_max = 0
            for i in range(len(heap)):
                cur_max = max(cur_max, heap[i][1])
            result.append((p, cur_max))
    return result


if __name__ == "__main__":
    print(skyline([(0, 3, 5), (1, 4, 3), (7, 8, 10), (6, 10, 4)]))
