def valid_ips_util(s, result, stack):
    if s == "" and len(stack) != 4:
        return

    if s != "" and len(stack) > 4:
        return

    if s == "" and len(stack) == 4:
        result.append(".".join(stack))
        return

    stack.append(s[:1])
    valid_ips_util(s[1:], result, stack)
    stack.pop()

    stack.append(s[:2])
    valid_ips_util(s[2:], result, stack)
    stack.pop()

    if int(s[:3]) < 256:
        stack.append(s[:3])
        valid_ips_util(s[3:], result, stack)
        stack.pop()


def valid_ips(s):
    result = []
    valid_ips_util(s, result, [])
    return result


if __name__ == "__main__":
    print(valid_ips("192168211"))
