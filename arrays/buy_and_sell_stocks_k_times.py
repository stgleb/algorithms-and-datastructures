# Given an array of stock prices over the time
# and k - max number of transactions to settle.
# Find out maximum profit from these at most K transactions.
def buy_and_sell_stocks_k_times(prices, k):
    profit = [[0 for _ in range(len(prices) + 1)] for _ in range(k + 1)]

    for i in range(1, k + 1):
        for j in range(1, len(prices)):
            max_so_far = 0
            for l in range(j):
                max_so_far = max(max_so_far, prices[j] - prices[l] + profit[i - 1][l])
            profit[i][j] = max(max_so_far, profit[i][j - 1])

    return profit[k][len(prices) - 1]


if __name__ == "__main__":
    print(buy_and_sell_stocks_k_times([10, 22, 5, 75, 65, 80], 2))
