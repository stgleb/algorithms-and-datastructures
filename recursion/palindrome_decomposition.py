def palindrome_decomposition(s):
    def decompose_util(text, decomposition, result):
        if len(text) == 0:
            result.append(decomposition.copy())
        for i in range(1, len(text) + 1):
            if text[:i] == ''.join(reversed(text[:i])):
                decomposition.append(text[:i])
                decompose_util(text[i:], decomposition, result)
                decomposition.pop()

    result = []
    decompose_util(s, [], result)
    return result


if __name__ == "__main__":
    print(palindrome_decomposition("1210343057887")[-1])
