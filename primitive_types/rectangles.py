def rectangle_contains(x1, y1, x2, y2, x, y):
    if x1 <= x <= x2 and y >= y1 and y <= y2:
        return True
    return False


def rectangles_intersect(x11, y11, x12, y12, x21, y21, x22, y22):
    if rectangle_contains(x11, y11, x12, y12, x21, y21):
        return True
    if rectangle_contains(x11, y11, x12, y12, x22, y22):
        return True
    if rectangle_contains(x11, y11, x12, y12, x21, y22):
        return True
    if rectangle_contains(x11, y11, x12, y12, x22, y21):
        return True

    if rectangle_contains(x21, y21, x22, y22, x11, y11):
            return True
    if rectangle_contains(x21, y21, x22, y22, x12, y12):
        return True
    if rectangle_contains(x21, y21, x22, y22, x11, y12):
        return True
    if rectangle_contains(x21, y21, x22, y22, x12, y11):
        return True

    return False


if __name__ == "__main__":
    print(rectangles_intersect(0, 0, 4, 4, 5, 5, 6, 6))
    print(rectangles_intersect(0, 0, 4, 4, 1, 1, 3, 3))
    print(rectangles_intersect(0, 0, 4, 4, 1, 1, 7, 6))
