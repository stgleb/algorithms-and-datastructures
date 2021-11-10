def palindromic_substring(s):
    table = [[0 for _ in range(len(s))] for _ in range(len(s))]
    for i in range(len(s)):
        table[i][i] = 1
        if i + 1 < len(s) and s[i] == s[i + 1]:
            table[i][i + 1] = 1
    n = len(s)
    k = 2
    max_len = 0
    start = 0
    end = 0
    j = 2
    while j < n:
        i = 0
        k = j
        while k < n:
            if s[i] == s[k] and table[i + 1][k - 1] == 1:
                table[i][k] = 1
                if k - i > max_len:
                    max_len = k - i
                    start = i
                    end = k
            k += 1
            i += 1
        j += 1

    return s[start:end + 1]


if __name__ == "__main__":
    print(palindromic_substring("geekeeforseek"))
    print(palindromic_substring("geekeegorseek"))