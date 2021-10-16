def build_view(heights):
    stack = []
    for i in reversed(range(len(heights))):
        if len(stack) == 0:
            stack.append(heights[i])
        else:
            while len(stack) > 0 and stack[-1] <= heights[i]:
                stack.pop()
            stack.append(heights[i])

    return stack[::-1]


if __name__ == "__main__":
    print(build_view([2, 3, 4, 1, 5, 3, 7, 9, 1, 3]))
