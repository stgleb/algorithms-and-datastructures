def is_palindromic_permutations(s):
    freq = {}
    for c in s:
        if c not in freq:
            freq[c] = 1
        else:
            freq[c] += 1

    counter = 0
    for key, value in freq.items():
        counter += value % 2
        if counter > 1:
            return False
    return True


if __name__ == "__main__":
    print(is_palindromic_permutations("edified"))
    print(is_palindromic_permutations("rotator"))
    print(is_palindromic_permutations("simultaneously"))
