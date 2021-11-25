def wildcard_match(text, pattern):
    if len(text) == 0 and len(pattern) == 0:
        return True
    if len(text) == 0 and len(pattern) > 0:
        return False
    if len(text) > 0 and len(pattern) == 0:
        return True
    if pattern[0] == ".":
        return wildcard_match(text[1:], pattern[1:])
    if pattern[0] == "*":
        for i in range(len(text)):
            if wildcard_match(text[i:], pattern[1:]):
                return True
    if pattern[0] != text[0]:
        return False

    return True


if __name__ == "__main__":
    text = "baaabab"
    pattern1 = "baaa?ab"
    pattern2 = "ba*a?"
    pattern3 = "a*ab"
    print(wildcard_match(text, pattern1))
    print(wildcard_match(text, pattern2))
    print(wildcard_match(text, pattern3))
