def see_and_say_util(number_str):
    i = 0
    result = []
    while i < len(number_str):
        j = i
        count = 0
        while j < len(number_str) and number_str[j] == number_str[i]:
            j += 1
            count += 1
        result.append(str(count))
        result.append(number_str[i])
        i = j
    return ''.join(result)


def see_and_say(n):
    cur = 1
    result = [cur]
    for i in range(n):
        next = see_and_say_util(str(cur))
        result.append(next)
        cur = next

    return result


if __name__ == "__main__":
    print(see_and_say(3))
    print(see_and_say(5))
    print(see_and_say(7))
