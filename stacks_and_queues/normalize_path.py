def normalize(path):
    terms = path.split('/')
    stack = []
    for t in terms:
        if t == ".":
            continue
        elif t == "":
            continue
        elif t == "..":
            if len(stack) > 0:
                stack.pop()
        elif t == "/":
            continue
        else:
            stack.append(t)

    if path[0] == "/":
        return "/" + '/'.join(stack)
    return '/'.join(stack)


if __name__ == "__main__":
    print(normalize("/usr/lib/../bin/gcc"))
    print(normalize("scripts//./../scripts/bash_scripts"))
    print(normalize("/foo/bar/./baz/../buzz"))
