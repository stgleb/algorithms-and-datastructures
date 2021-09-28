import random


def offline_random_sampling(stream, buffer_size):
    i = 0
    sample = []
    for v in stream:
        if i < buffer_size:
            sample.append(v)
        else:
            rand_index = random.randint(0, i)
            if rand_index < buffer_size:
                sample[rand_index] = v
        i += 1

    return sample


if __name__ == "__main__":
    number_of_tests = 10000
    freq = dict()

    for i in range(number_of_tests):
        sample = offline_random_sampling([i for i in range(100)], 10)
        for v in sample:
            if v in freq:
                freq[v] += 1
            else:
                freq[v] = 1

    print(freq)
