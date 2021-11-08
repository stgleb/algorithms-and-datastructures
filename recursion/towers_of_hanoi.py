def check(f, t, a):
    for i in range(len(f) - 1):
        if f[i] < f[i + 1]:
            return False

    for i in range(len(t) - 1):
        if t[i] < t[i + 1]:
            return False

    for i in range(len(a) - 1):
        if a[i] < a[i + 1]:
            return False

    return True


def solve(n, from_tower, to_tower, aux_tower):
    if not check(from_tower, to_tower, aux_tower):
        print("FAIL")
        return
    if n > 0:
        solve(n - 1, from_tower, aux_tower, to_tower)
        print("from:", from_tower, "to:", to_tower, "aux:", aux_tower)
        to_tower.append(from_tower.pop())
        solve(n - 1, aux_tower, to_tower, from_tower)


if __name__ == "__main__":
    n = 6
    from_tower = list(reversed([i for i in range(n)]))
    aux_tower = []
    to_tower = []
    solve(n, from_tower, aux_tower, to_tower)
    print(from_tower, to_tower, aux_tower)

