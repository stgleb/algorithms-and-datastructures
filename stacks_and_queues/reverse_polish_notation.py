def add(x, y):
    return x + y


def mul(x, y):
    return x * y


def sub(x, y):
    return x - y


def div(x, y):
    return x / y


operations = {"+": add, "-": sub, "*": mul, "/": div}


def rpn_compute(expression):
    stack = []
    for term in expression:
        if term in operations:
            op1 = stack[-1]
            op2 = stack[-2]
            operation = operations[term]
            result = operation(op1, op2)
            stack.append(result)
        else:
            stack.append(term)

    return stack[-1]


if __name__ == "__main__":
    print(rpn_compute([2, 3, "+", 4, "*"]))
