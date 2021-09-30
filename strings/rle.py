def rle(s):
    i = 0
    result = []
    while i < len(s):
        j = i
        count = 0
        while j < len(s) and s[j] == s[i]:
            j += 1
            count += 1
        if count > 1:
            result.append(str(count))
        result.append(s[i])
        i = j
    return "".join(result)


if __name__ == "__main__":
    print(rle("afafaababababaaaabababa"))
    print(rle("abaaacabcccabaa"))
