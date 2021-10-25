def closest_repeating_element(a):
    distances = {}
    closest = len(a)
    for i in range(len(a)):
        if a[i] not in distances:
            distances[a[i]] = i
        else:
            if i - distances[a[i]] < closest:
                closest = i - distances[a[i]]
            distances[a[i]] = i

    return closest


if __name__ == "__main__":
    print(closest_repeating_element([1, 2, 3, 4, 5, 6, 2, 5, 7, 8]))

