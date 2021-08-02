
NUM_SIZE = 64


def closest_number(num):
    for i in range(NUM_SIZE):
        if num >> i & 1 != num >> (i + 1) & 1:
            num ^= 1 << i | 1 << (i + 1)
            return num
    return num


if __name__ == "__main__":
    print(closest_number(10))
    print(closest_number(14))
    print(closest_number(11))
    print(closest_number(6))
