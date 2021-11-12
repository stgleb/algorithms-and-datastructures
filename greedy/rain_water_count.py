def count_trap_water(heights):
    total = 0
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


if __name__ == "__main__":
    print(count_trap_water([4, 3, 1, 5, 1]))
