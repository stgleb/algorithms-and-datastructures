def count_bits(num):
    cnt = 0
    while num:
        num = num & num - 1
        cnt += 1
    return cnt


if __name__ == "__main__":
    print(count_bits(5))
    print(count_bits(7))
    print(count_bits(11))
