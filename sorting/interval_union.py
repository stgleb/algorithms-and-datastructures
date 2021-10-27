def interval_union(intervals):
    points = []
    for start, end in intervals:
        points.append((start, 1))
        points.append((end, -1))
    points = sorted(points)
    cur = 0
    start, end = points[0][0], points[0][0]
    result = []
    for point, val in points:
        if cur == 0:
            start = point
        cur += val
        end = point
        if cur == 0:
            result.append((start, end))
    return result


if __name__ == "__main__":
    print(interval_union([(1, 5), (2, 7), (4, 5), (8, 9), (6, 10), (17, 18), (14, 15), (11, 13), (14, 15), (9, 15)]))

