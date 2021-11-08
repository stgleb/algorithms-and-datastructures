numbers = {"1": "", "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
           "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}


def decode_number_util(number, current, result):
    if len(number) == 0:
        result.append(current.copy())
        return
    letters = numbers[number[0]]
    for l in letters:
        current.append(l)
        decode_number_util(number[1:], current, result)
        current.pop()


def decode_number(number):
    result = []
    decode_number_util(number, [], result)
    return ["".join(s) for s in result]


if __name__ == "__main__":
    print(decode_number("326484"))
