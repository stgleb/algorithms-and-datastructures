import math


def primes(n):
    is_prime = [True for _ in range(n)]
    num = int(math.sqrt(n) + 1)
    for i in range(2, num + 1):
        for j in range(i * 2, n, i):
            is_prime[j] = False

    return [x for x in range(len(is_prime)) if is_prime[x]]


if __name__ == "__main__":
    print(primes(100))
