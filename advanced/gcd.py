def gcd(a, b):
    if a == 0:
        return b
    if b == 0:
        return a
    if a == b:
        return a
    if a < b:
        return gcd(b - a, a)
    return gcd(a - b, b)


def gcd_no_op(a, b):
    if not a & 1 and not b & 1:
        return gcd(a >> 1, b >> 1) << 1
    if not a & 1:
        return gcd(a >> 1, b)
    if not b & 1:
        return gcd(a, b >> 1)
    if a > b:
        return gcd(a - b, b)
    return gcd(b - a, a)


if __name__ == "__main__":
    print(gcd(300, 100))
    print(gcd_no_op(300, 100))

    print(gcd(27, 12))
    print(gcd_no_op(27, 12))

    print(gcd(36, 18))
    print(gcd_no_op(36, 18))

    print(gcd(54, 36))
    print(gcd_no_op(54, 36))
