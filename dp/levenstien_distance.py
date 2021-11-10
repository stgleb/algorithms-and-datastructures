def levenstien_distance_rec(s1, s2):
    if len(s1) == 0:
        return len(s2)
    if len(s2) == 0:
        return len(s1)
    if s1[0] == s2[0]:
        return levenstien_distance_rec(s1[1:], s2[1:])
    return min(levenstien_distance_rec(s1[1:], s2),
               levenstien_distance_rec(s1, s2[1:]),
               levenstien_distance_rec(s1[1:], s2[1:])) + 1


def levenstien_distance_mem(s1, s2):
    table = [[0 for _ in range(len(s2) + 1)] for _ in range(len(s1) + 1)]
    for i in range(len(s1) + 1):
        for j in range(len(s2) + 1):
            if i == 0:
                table[i][j] = j
            elif j == 0:
                table[i][j] = i
            elif s1[i - 1] == s2[j - 1]:
                table[i][j] = table[i - 1][j - 1]
            else:
                table[i][j] = 1 + min(table[i][j - 1], table[i - 1][j], table[i - 1][j - 1])

    return table[len(s1)][len(s2)]


if __name__ == "__main__":
    print(levenstien_distance_rec("barbaris", "baracuda"))
    print(levenstien_distance_mem("barbaris", "baracuda"))

