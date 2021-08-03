def multiply(a, b):
    result = 0
    i = 0
    while b >= (1 << i):
        if b & (1 << i):
            result = result + (a << i)
        i += 1
    return result


if __name__ == "__main__":
    print(multiply(2, 3))
    print(multiply(7, 8))

