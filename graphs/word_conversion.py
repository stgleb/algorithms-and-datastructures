def build_graph(words):
    graph = {w: [] for w in words}
    alphabet = [chr(i + ord('a')) for i in range(26)] + ['']

    for w in words:
        for i in range(len(w)):
            for c in alphabet:
                new_word = w[:i] + c + w[i + 1:]
                if new_word in words:
                    graph[w].append(new_word)
    return graph


def transform(word1, word2, graph):
    q = [[word1]]
    while q:
        cur = q[0]
        q = q[1:]
        adjacent_wors = graph[cur[-1]]
        for w in adjacent_wors:
            if w == word2:
                return cur + [w]
            if w not in cur:
                q.append(cur + [w])
    return None


if __name__ == "__main__":
    words = ["poon", "plee", "same", "some", "spoon", "sponge", "spam",
             "span", "spin", "toon", "poie", "plea", "plie", "poin", "pion"]
    print(transform("toon", "plie", build_graph(words)))
