def biggest_product_without_one(a):
    max_negative = float('-inf')
    min_positive = float('inf')
    min_negative = float('inf')

    count_zeros = 0
    count_negative = 0
    count_positive = 0
    product = 1

    for i in range(len(a)):
        if a[i] == 0:
            count_zeros += 1
        elif a[i] < 0:
            product = product * a[i]
            count_negative += 1
            max_negative = max(max_negative, a[i])
            min_negative = min(min_negative, a[i])
        else:
            product = product * a[i]
            count_positive += 1
            min_positive = min(min_positive, a[i])
    if count_zeros > 1:
        return 0

    if count_zeros == 1:
        return product

    if count_positive == 0 and count_negative % 2 == 0:
        return product / min_negative

    if count_positive > 0 and count_negative % 2 == 0:
        return product / min_positive

    if count_positive > 0 and count_negative % 2:
        return product / max_negative

    if count_negative == 0:
        return product / min_positive

    return product


if __name__ == "__main__":
    print(biggest_product_without_one([-1, -2, 0, 2, 3]))
    print(biggest_product_without_one([-1, 0, -2, 0, 2, 3]))
    print(biggest_product_without_one([-1, -2, -10, -20, 1, 2, 3]))
    print(biggest_product_without_one([-1, -2, -3, -4]))
