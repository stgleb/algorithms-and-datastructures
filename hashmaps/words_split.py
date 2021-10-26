def words_split(text, words):
    while text:
        flag = False
        for w in words:
            if text.startswith(w):
                text = text[len(w):]
                flag = True
        if not flag:
            return False
    return True
        

if __name__ == "__main__":
    print(words_split("alpcanana", {"can", "alp", "ana"}))
