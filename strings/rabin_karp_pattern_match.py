import functools


def rabin_karp(s, t):
    base = 26
    h_t = functools.reduce(lambda h, c: h * base + ord(c), t[:len(s)], 0)
    h_s = functools.reduce(lambda h, c: h * base + ord(c), s, 0)
    power_s = base ** (len(s) - 1)

    for i in range(len(s), len(t)):
        if h_t == h_s and t[i - len(s):i] == s:
            return i - len(s)

        h_t -= power_s * ord(t[i - len(s)])
        h_t = h_t * base + ord(t[i])

    if h_t == h_s and t[- len(s):] == s:
        return len(t) - len(s)

    return -1


if __name__ == "__main__":
    print(rabin_karp("abc", "ababcaaa"))
    print(rabin_karp("abba", "caabba"))
