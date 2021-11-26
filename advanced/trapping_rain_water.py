def trap_water(a):
    start, end = 0, len(a) - 1
    left_max = a[start]
    right_max = a[end]
    trap = 0
    while start < end:
        if left_max < right_max:
            trap += left_max - a[start]
            start += 1
            left_max = max(left_max, a[start])
        else:
            trap += right_max - a[end]
            end -= 1
            right_max = max(right_max, a[end])
    return trap


if __name__ == "__main__":
    print(trap_water([4, 3, 1, 5, 1]))
    print(trap_water([4, 3, 1, 5, 1]))
