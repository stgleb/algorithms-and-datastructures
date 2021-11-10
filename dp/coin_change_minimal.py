import sys


def coin_change_minimal_rec(coins, number):
    if number == 0:
        return 0
    result = sys.maxsize
    for i in range(len(coins)):
        if coins[i] <= number:
            tmp_result = coin_change_minimal_rec(coins, number - coins[i])
            if tmp_result != sys.maxsize and tmp_result + 1 < result:
                result = tmp_result + 1
    return result


def coin_change_minimal_mem(coins, number):
    table = [sys.maxsize for _ in range(number + 1)]
    table[0] = 0

    for i in range(1, number + 1):
        j = 0
        while j < len(coins) and coins[j] <= i:
            if table[i - coins[j]] != sys.maxsize and table[i] > table[i - coins[j]] + 1:
                table[i] = table[i - coins[j]] + 1
            j += 1
    return table[number]


if __name__ == "__main__":
    print(coin_change_minimal_rec([2, 3, 7], 10))
    print(coin_change_minimal_mem([2, 3, 7], 10))
    print(coin_change_minimal_rec([1, 2, 3, 5], 16))
    print(coin_change_minimal_mem([1, 2, 3, 5], 16))

