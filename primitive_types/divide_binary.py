def divide(a, b):
    result, power = 0, 8
    while a >= b:
        while a < (1 << power) * b:
            power -= 1
        a = a - (1 << power) * b
        result += (1 << power)
    return result


if __name__ == "__main__":
    print(divide(44, 7))
    print(divide(29, 3))
    print(divide(64, 8))
