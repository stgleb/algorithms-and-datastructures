def sequential_subarray(text, words):
    text = text.split(" ")
    subarray_len = [float("inf")] * len(words)
    latest_occurence = [float("inf")] * len(words)
    word2index = {}

    for i in range(len(words)):
        word2index[words[i]] = i

    for i in range(len(text)):
        w = text[i]
        if w in word2index:
            index = word2index[w]
            if index == 0:
                subarray_len[index] = 1
            elif subarray_len[index - 1] != float("inf"):
                distance_to_prev = i - latest_occurence[index - 1]
                subarray_len[index] = distance_to_prev + subarray_len[index - 1]
            latest_occurence[index] = i

    return subarray_len[len(words) - 1]


if __name__ == "__main__":
    print(sequential_subarray("paramount object in the struggle is to save the union and "
                                "is not either union destroy or save slavery",
                                ["save", "union", "slavery"]))
