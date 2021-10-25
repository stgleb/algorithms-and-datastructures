def is_anonymous_constructable(text, letter):
    text_freq = {}
    letter_freq = {}

    for c in text:
        if c not in text_freq:
            text_freq[c] = 1
        else:
            text_freq[c] += 1

    for c in letter:
        if c not in letter_freq:
            letter_freq[c] = 1
        else:
            letter_freq[c] += 1

    for key, val in letter_freq.items():
        if key not in text_freq or text_freq[key] < letter_freq[key]:
            return False
    return True


if __name__ == "__main__":
    print(is_anonymous_constructable("one two three four five six seven eight nine ten eleven twelve", "hello"))
    print(is_anonymous_constructable("one two three four five six seven eight nine ten eleven twelve", "several things"))
    print(is_anonymous_constructable("one two three four five six seven eight nine ten eleven twelve", "high level"))
    print(is_anonymous_constructable("one two three four five six seven eight nine ten eleven twelve", "high nest"))

