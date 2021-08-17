# Given an array of stock prices - compute the best
# time to buy and then sell stocks twice to maximize profit.

def buy_and_sell_twice(prices):
    profit_left = [0 for _ in range(len(prices))]
    profit_right = [0 for _ in range(len(prices))]

    # max profit sliding from left to right
    min_so_far = prices[0]
    max_profit = 0
    for i in range(len(prices)):
        if prices[i] < min_so_far:
            min_so_far = prices[i]
        if prices[i] - min_so_far > max_profit:
            max_profit = prices[i] - min_so_far
        profit_left[i] = max_profit

    # max profit sliding from right to left
    max_so_far = prices[len(prices) - 1]
    max_profit = 0
    for i in range(len(prices) - 1, -1, -1):
        if prices[i] > max_so_far:
            max_so_far = prices[i]
        if max_so_far - prices[i] > max_profit:
            max_profit = max_so_far - prices[i]
        profit_right[i] = max_profit

    # select max profit for both deals
    max_profit_twice = 0
    for i in range(0, len(prices) - 2):
        max_profit_twice = max(max_profit_twice, profit_left[i] + profit_right[i + 1])

    return max_profit_twice, profit_left, profit_right


if __name__ == "__main__":
    print(buy_and_sell_twice([210, 130, 100, 80, 90, 200, 110, 150, 70]))
