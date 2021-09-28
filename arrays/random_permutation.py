import random


def random_sampling(k, numbers):
    for i in range(k):
        random_index = random.randint(0, i)
        numbers[i], numbers[random_index] = numbers[random_index], numbers[i]
        i += 1
    return numbers[:k + 1]


if __name__ == "__main__":
    print(random_sampling(10, [i for i in range(10)]))
