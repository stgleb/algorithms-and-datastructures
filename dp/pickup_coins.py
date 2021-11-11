def pickup_coin_util(coins, your_turn):
    if len(coins) == 0:
        return 0

    if len(coins) == 1 and your_turn:
        return coins[0]
    elif len(coins) == 1:
        return 0

    if your_turn:
        return max(pickup_coin_util(coins[1:], not your_turn) + coins[0],
                   pickup_coin_util(coins[:len(coins) - 1], not your_turn) + coins[-1])
    else:
        return min(pickup_coin_util(coins[1:], not your_turn),
                   pickup_coin_util(coins[:len(coins) - 1], not your_turn))


def pickup_coins_rec(coins):
    return pickup_coin_util(coins, True)


def pickup_coin_mem(coins):
    n = len(coins)
    table = [[0] * n for _ in range(n)]
    for i in range(len(coins)):
        table[i][i] = coins[i]
        if i + 1 < n:
            table[i][i + 1] = max(coins[i], coins[i + 1])

    j = 1
    if n % 2 == 0:
        your_turn = True
    else:
        your_turn = False

    while j < n:
        i = 0
        k = j
        while k < n:
            if your_turn:
                table[i][k] = max(table[i + 1][k] + coins[i], table[i][k - 1] + coins[k])
            else:
                table[i][k] = min(table[i + 1][k], table[i][k - 1])
            i += 1
            k += 1
        your_turn = not your_turn
        j += 1
    return table[0][n - 1]


if __name__ == "__main__":
    print(pickup_coins_rec([25, 5, 10, 10, 15, 20, 5]))
    print(pickup_coin_mem([25, 5, 10, 10, 15, 20, 5]))
