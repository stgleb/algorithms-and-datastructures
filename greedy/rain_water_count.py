def count_trap_water(heights):
    n = len(heights)
    left_max = [0 for _ in range(n)]
    right_max = [0 for _ in range(n)]
    cur_max = 0
    for i in range(n):
        if heights[i] > cur_max:
            cur_max = heights[i]
        left_max[i] = cur_max

    cur_max = 0
    for i in reversed(range(len(heights))):
        if heights[i] > cur_max:
            cur_max = heights[i]
        right_max[i] = cur_max

    total = 0
    for i in range(n):
        total += min(left_max[i], right_max[i]) - heights[i]
    return total


def count_trap_water2(heights):
    left_max = heights[0]
    right_max = heights[-1]
    n = len(heights) - 1
    i, j = 0, n
    total = 0

    while i < j:
        if left_max < right_max:
            total += left_max - heights[i]
            i += 1
            left_max = max(heights[i], left_max)
        else:
            total += right_max - heights[j]
            j -= 1
            right_max = max(heights[j], right_max)
    return total


if __name__ == "__main__":
    print(count_trap_water([4, 3, 1, 5, 1]))
    print(count_trap_water2([4, 3, 1, 5, 1]))
