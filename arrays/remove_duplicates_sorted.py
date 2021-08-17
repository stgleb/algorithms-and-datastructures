# Given an array of sorted elements, remove all duplicates
# and shift remaining elements to left.

def remove_duplicates(a):
    next_index = 1
    for i in range(len(a)):
        if a[i] != a[next_index - 1]:
            a[i], a[next_index] = a[next_index], a[i]
            next_index += 1
    return a[:next_index]
    

if __name__ == "__main__":
    print(remove_duplicates([1, 1, 2, 3, 3, 4, 5, 5, 5]))

