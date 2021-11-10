
def coin_change_rec_util(coins, m, number):
    if m == 0 and number > 0:
        return 0

    if number == 0:
        return 1

    if number < 0:
        return 0

    return coin_change_rec_util(coins, m - 1, number) + coin_change_rec_util(coins, m, number - coins[m - 1])


def coin_change_number_of_ways_rec(coins, number):
    return coin_change_rec_util(coins, len(coins), number)


def coin_change_number_of_ways_mem(coins, number):
    table = [[0 for _ in range(len(coins))] for _ in range(number + 1)]
    for i in range(len(table)):
        for j in range(len(table[i])):
            if i == 0:
                table[i][j] = 1
            else:
                if j > 0:
                    table[i][j] += table[i][j - 1]
                if coins[j] <= i:
                    table[i][j] += table[i - coins[j]][j]
    return table[number][len(coins) - 1]


if __name__ == "__main__":
    print(coin_change_number_of_ways_rec([2, 3, 7], 10))
    print(coin_change_number_of_ways_mem([2, 3, 7], 10))
    print(coin_change_number_of_ways_rec([1, 2, 5, 10], 12))
    print(coin_change_number_of_ways_mem([1, 2, 5, 10], 12))
