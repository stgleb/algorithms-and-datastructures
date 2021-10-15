def validate_parenthesis(expression):
    lst = list(expression)
    stack = []
    open = {'(', '[', '{'}
    close = {')': '(', ']': '[', '}': '{'}
    for p in lst:
        if p in open:
            stack.append(p)
        elif p in close:
            if len(stack) == 0 or stack[-1] != close[p]:
                return False
            else:
                stack.pop()
        else:
            return False
    return len(stack) == 0


if __name__ == "__main__":
    print(validate_parenthesis("(())"))
    print(validate_parenthesis("(({[]}))[](){}"))
    print(validate_parenthesis("[[(){}]]"))
    print(validate_parenthesis("((()"))
