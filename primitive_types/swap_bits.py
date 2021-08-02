def swap_bits(num, i, j):
    if num & (1 << i) != num & (1 << j):
        num ^= 1 << i
        num ^= 1 << j
    return num


if __name__ == "__main__":
    print(swap_bits(5, 0, 1))

