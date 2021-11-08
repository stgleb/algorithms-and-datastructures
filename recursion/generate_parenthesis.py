def check_valid(exp):
    o = 0
    for c in exp:
        if c == '(':
            o += 1
        else:
            o -= 1
        if o < 0:
            return False

    if o != 0:
        return False
    return True


def generate_util(exp, i, n, result):
    if i == n:
        if check_valid(exp):
            result.append(exp.copy())
        return
    exp[i] = ')'
    generate_util(exp, i + 1, n, result)
    exp[i] = '('
    generate_util(exp, i + 1, n, result)


def generate_parenthesis(n):
    result = []
    parenthesis = [' ' for _ in range(2*n)]
    generate_util(parenthesis, 0, n * 2, result)
    return ["".join(r) for r in result]


def generate_parenthesis_util2(left, right, cur, result):
    if left > 0:
        generate_parenthesis_util2(left - 1, right, cur + "(", result)

    if right > left:
        generate_parenthesis_util2(left, right - 1, cur + ")", result)

    if right == 0:
        result.append(cur)


def generate_parenthesis2(n):
    result = []
    generate_parenthesis_util2(n, n, "", result)
    return ["".join(r) for r in result]


if __name__ == "__main__":
    print(generate_parenthesis(3))
    print(generate_parenthesis2(3))
