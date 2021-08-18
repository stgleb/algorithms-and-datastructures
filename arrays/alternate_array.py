# Given an array of numbers, rearrange elements to specific order
#
# A1 <== A2 >= A3 <= A4 >= A5 ...

def alternate_array(a):
    for i in range(len(a) - 1):
        if i % 2 == 0 and a[i] >= a[i + 1]:
            a[i], a[i + 1] = a[i + 1], a[i]
        if i % 2 != 0 and a[i] <= a[i + 1]:
            a[i], a[i + 1] = a[i + 1], a[i]
    return a


if __name__ == "__main__":
    print(alternate_array([5, 2, 7, 4, 1, 6, 3]))

