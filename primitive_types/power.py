def power(x, y):
    result = 1
    while y:
        if y & 1:
            result *= x
            y -= 1
        else:
            x = x * x
            y >>= 1

    return result


if __name__ == "__main__":
    print(power(2, 32))
    print(power(3, 4))
    print(power(5, 3))
    print(power(52352452, 0))

