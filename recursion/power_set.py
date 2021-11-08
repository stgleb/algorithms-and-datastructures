def power_set_util(elements, i, selection,  result):
    if i == len(elements):
        result.append([v for v in selection.values()])
        return
    selection[i] = elements[i]
    power_set_util(elements, i + 1, selection, result)
    del selection[i]
    power_set_util(elements, i + 1, selection, result)


def power_set(elements):
    result = []
    selection = {}
    power_set_util(elements, 0, selection, result)
    return result


if __name__ == "__main__":
    print(power_set([1, 2, 3]))
