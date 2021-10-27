def merge(A, B, a_len):
    write_index = len(A) - 1
    a, b = a_len - 1, len(B) - 1

    while a >= 0 and b >= 0:
        if A[a] > B[b]:
            A[write_index] = A[a]
            a -= 1
        else:
            A[write_index] = B[b]
            b -= 1
        write_index -= 1
    return A


if __name__ == "__main__":
    print(merge([1, 3, 5, 6, -1, -1, -1, -1], [2, 4, 7, 9], 4))
