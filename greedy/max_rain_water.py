def max_rain_water(heights):
    i, j = 0, len(heights) - 1
    max_trap = 0
    max_left = 0
    max_right = 0
    while i < j:
        if max_trap < min(heights[i], heights[j]) * (j - i + 1):
            max_trap = min(heights[i], heights[j]) * (j - i + 1)
            max_left = i
            max_right = j
        if heights[i] < heights[j]:
            i += 1
        else:
            j -= 1
    return max_left, max_right


if __name__ == "__main__":
    print(max_rain_water([2, 1, 3, 4, 2, 8, 1, 7, 9, 3]))
