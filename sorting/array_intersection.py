def intersection(a, b):
    a = sorted(a)
    b = sorted(b)
    i = 0
    j = 0
    result = []

    while i < len(a) and j < len(b):
        if a[i] == b[j]:
            result.append(a[i])
            i += 1
            j += 1
        elif a[i] < b[j]:
            i += 1
        else:
            j += 1
    
    return result


if __name__ == "__main__":
    print(intersection([2, 1, 5, 4, 8, 9, 3], [1, 8, 9, 6, 5, 7, 3]))
