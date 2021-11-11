def lcs_rec(s1, s2):
    if len(s1) == 0 or len(s2) == 0:
        return 0
    if s1[0] == s2[0]:
        return lcs_rec(s1[1:], s2[1:]) + 1
    return max(lcs_rec(s1[1:], s2), lcs_rec(s1, s2[1:]))


def lcs_mem(s1, s2):
    n = len(s1)
    m = len(s2)
    table = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(m + 1):
            if i == 0 or j == 0:
                table[i][j] = 0
            elif s1[i - 1] == s2[j - 1]:
                table[i][j] = 1 + table[i - 1][j - 1]
            else:
                table[i][j] = max(table[i][j - 1], table[i - 1][j])

    return table[n][m]


if __name__ == "__main__":
    print(lcs_rec("AGGTACAAG", "GTACTACTAT"))
    print(lcs_mem("AGGTACAAG", "GTACTACTAT"))
