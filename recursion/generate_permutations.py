def gen_permutations_util(a, i, result):
    if i == len(a) - 1:
        result.append(a.copy())
        return
    for j in range(i, len(a)):
        a[i], a[j] = a[j], a[i]
        gen_permutations_util(a, i + 1, result)
        a[i], a[j] = a[j], a[i]


def generate_permutations(a):
    result = []
    gen_permutations_util(a, 0, result)
    return result


if __name__ == "__main__":
    print(generate_permutations([1, 2, 3, 4]))
