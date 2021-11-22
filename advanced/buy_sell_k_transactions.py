def buy_sell_stocks(a, k):
    n = len(a)
    profit = [[0] * (k + 1) for _ in range(n)]

    for i in range(1, n):
        for j in range(1, k + 1):
            max_so_sar = 0
            for l in range(i):
                max_so_sar = max(max_so_sar, a[i] - a[l] + profit[l][j - 1])

            profit[i][j] = max(max_so_sar, profit[i - 1][j])
    return profit[n - 1][k]


if __name__ == "__main__":
    k = 2
    prices = [10, 22, 5, 75, 65, 80]
    print(buy_sell_stocks(prices, k))
