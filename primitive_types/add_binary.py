def add(a, b):
    while b:
        carry = (a & b) << 1
        a = a ^ b
        b = carry
    return a


if __name__ == "__main__":
    print(add(3, 2))
    print(add(17, 4))
