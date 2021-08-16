# Given an array of non-negative integers where each integer
# represents maximum number of hops forward. Find out if the last
# element of the array is reachable.
def is_reachable(a):
    last_reachable, i = 0, 0
    while last_reachable >= i and i < len(a):
        last_reachable = max(i + a[i], last_reachable)
        i += 1

    return last_reachable >= len(a) - 1


if __name__ == "__main__":
    print(is_reachable([1, 2, 1, 1, 2, 0, 0]))
