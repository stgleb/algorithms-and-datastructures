def max_overlap(intervals):
    points = []
    for start, end in intervals:
        points.append((start, 1))
        points.append((end, -1))

    cur = 0
    max_overlap_val = 0
    points = sorted(points)
    for point, val in points:
        cur += val
        if cur > max_overlap_val:
            max_overlap_val = cur
    return max_overlap_val


if __name__ == "__main__":
    print(max_overlap([(1, 5), (2, 7), (4, 5), (8, 9), (6, 10), (9, 18), (12, 15), (11, 13), (14, 15), (9, 15)]))

