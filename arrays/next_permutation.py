def next_permutation(perm):
    inversion_point = len(perm) - 2
    while inversion_point >= 0 and perm[inversion_point] > perm[inversion_point + 1]:
        inversion_point -= 1

    # permutation has highest lex order.
    if inversion_point == -1:
        return perm

    for i in reversed(range(inversion_point + 1, len(perm))):
        if perm[i] > perm[inversion_point]:
            perm[i], perm[inversion_point] = perm[inversion_point], perm[i]
            break

    perm[inversion_point + 1:] = reversed(perm[inversion_point + 1:])
    return perm


if __name__ == "__main__":
    print(next_permutation([1, 2, 4, 3, 5]))
    print(next_permutation([1, 4, 5, 3, 2]))
    print(next_permutation([4, 3, 1, 5, 2]))
