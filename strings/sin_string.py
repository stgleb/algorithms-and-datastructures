def print_string_sin(s):
    s1 = [' ' for _ in range(len(s))]
    s2 = [' ' for _ in range(len(s))]
    s3 = [' ' for _ in range(len(s))]

    for i in range(1, len(s), 4):
        s1[i] = s[i]

    for i in range(0, len(s), 2):
        s2[i] = s[i]

    for i in range(3, len(s), 4):
        s3[i] = s[i]

    print(s1)
    print(s2)
    print(s3)


if __name__ == "__main__":
    print_string_sin("hello, world!!!")
