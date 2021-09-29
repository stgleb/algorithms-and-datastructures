def replace_and_remove(size, cap, arr):
    while size > -1:
        if arr[size - 1] == 'a':
            arr[cap - 1] = 'd'
            arr[cap - 2] = 'd'
            cap -= 2
        elif arr[size - 1] != 'b':
            arr[cap - 1] = arr[size - 1]
            cap -= 1
        size -= 1
    return ''.join(arr)


if __name__ == "__main__":
    print(replace_and_remove(4, 5, ['a', 'b', 'b', 'c', '']))
