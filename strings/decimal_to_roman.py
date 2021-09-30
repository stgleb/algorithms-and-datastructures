dec = [1000, 500, 100, 50, 10, 5, 1]
roman = ["M", "D", "C", "L", "X", "V", "I"]


def dec_to_roman(n):
    i = 0
    result = []
    while i < len(dec):
        for _ in range(n // dec[i]):
            n -= dec[i]
            result.append(roman[i])
        i += 1
    return "".join(result)


if __name__ == "__main__":
    print(dec_to_roman(1492))
    print(dec_to_roman(1904))
    print(dec_to_roman(1657))
