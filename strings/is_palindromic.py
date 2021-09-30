def is_palindromic(sentence):
    i, j = 0, len(sentence) - 1

    while i < j:
        while i < j and not sentence[i].isalnum():
            i += 1
        while i < j and not sentence[j].isalnum():
            j -= 1
        if sentence[i].lower() != sentence[j].lower():
            return False
        i, j = i + 1, j - 1

    return True


if __name__ == "__main__":
    print(is_palindromic("Mr. Owl ate my metal worm"))
    print(is_palindromic("Was it a car or a cat I saw?"))
    print(is_palindromic("Was it a car or a pot I saw"))
