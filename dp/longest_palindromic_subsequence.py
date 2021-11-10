def longest_palindromic_subsequence_rec(s):
    if len(s) == 0:
        return 0
    if len(s) == 1:
        return 1
    if len(s) == 2 and s[0] == s[1]:
        return 2
    elif len(s) == 2:
        return 1
    if s[0] == s[-1]:
        return longest_palindromic_subsequence_rec(s[1:len(s) - 1]) + 2
    return max(longest_palindromic_subsequence_rec(s[1:]), longest_palindromic_subsequence_rec(s[:len(s) - 1]))


def longest_palindromic_subsequence_mem(s):
    n = len(s)
    table = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        table[i][i] = 1
        if i < n - 1 and s[i] == s[i + 1]:
            table[i][i + 1] = 2
        elif i < n - 1 and s[i] != s[i + 1]:
            table[i][i + 1] = 1
    j = 2
    while j < n:
        i = 0
        k = j
        while k < n:
            if s[i] == s[k]:
                table[i][k] = table[i + 1][k - 1] + 2
            else:
                table[i][k] = max(table[i + 1][k], table[i][k - 1])
            k += 1
            i += 1
        j += 1
    return table[0][n - 1]


if __name__ == "__main__":
    print(longest_palindromic_subsequence_rec("geeks for geeks"))
    print(longest_palindromic_subsequence_mem("geeks for geeks"))
