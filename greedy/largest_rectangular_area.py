def max_rectangular_area(heights):
    heights = heights
    n = len(heights) - 1
    stack = []
    max_area = 0
    l, r = 0, 0
    for i in range(n):
        while stack and heights[stack[-1]] >= heights[i]:
            h = heights[stack.pop()]
            w = i if not stack else i - stack[-1] - 1
            new_area = h * w
            if max_area < new_area:
                max_area = new_area
                r = i - 1
                l = 0 if not stack else stack[-1] + 1
        stack.append(i)

    while stack:
        h = heights[stack.pop()]
        w = len(heights) if not stack else len(heights) - stack[-1] - 1
        new_area = h * w
        if max_area < new_area:
            max_area = new_area
            r = len(heights) - 1
            l = 0 if not stack else stack[-1] + 1
    return [l, r], max_area


if __name__ == "__main__":
    print(max_rectangular_area([6, 2, 5, 4, 4, 5, 1, 6, 6, 6]))
