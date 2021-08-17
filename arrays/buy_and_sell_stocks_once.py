# Given an array of stock prices - compute the best
# time to buy and then sell stocks to maximize profit.

def buy_and_sell(prices):
    min_index, time_to_buy, time_to_sell, max_profit = 0, 0,  0, 0
    for i in range(len(prices)):
        if prices[i] < prices[min_index]:
            min_index = i
        if prices[i] - prices[min_index] > max_profit:
            max_profit = prices[i] - prices[min_index]
            time_to_sell = i
            time_to_buy = min_index
    return max_profit, time_to_buy, time_to_sell


if __name__ == "__main__":
    print(buy_and_sell([210, 130, 100, 80, 90, 200, 110, 150, 70]))
