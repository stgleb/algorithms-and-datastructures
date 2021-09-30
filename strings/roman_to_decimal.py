roman_digit = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000,
}


def roman_to_decimal(roman_number):
    i = len(roman_number) - 1
    j = len(roman_number) - 2
    result = 0
    while i >= 0:
        result += roman_digit[roman_number[i]]
        while j >= 0 and roman_digit[roman_number[j]] < roman_digit[roman_number[i]]:
            result -= roman_digit[roman_number[j]]
            j -= 1
        i = j
        j = i - 1

    return result


if __name__ == "__main__":
    print(roman_to_decimal("MCMIV"))
    print(roman_to_decimal("XIX"))
    print(roman_to_decimal("MCDXCII"))
    print(roman_to_decimal("IV"))
