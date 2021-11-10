
def knapsack_problem_rec(weights, prices, capacity):
    if capacity < 0:
        return -1

    max_profit = 0
    for i in range(len(weights)):
        res = knapsack_problem_rec(weights, prices, capacity - weights[i])
        if res != -1:
            max_profit = max(res + prices[i], max_profit)

    return max_profit


def knapsack_mem(weights, prices, capacity):
    table = [[-1 for _ in range(len(weights))] for _ in range(capacity + 1)]

    for i in range(capacity + 1):
        for j in range(len(table[i])):
            max_profit = 0
            if i - weights[j] >= 0:
                max_profit = max(max_profit, table[i - weights[j]][j] + prices[j])
            if j > 0:
                max_profit = max(max_profit, table[i][j - 1])
            table[i][j] = max_profit
    return table[capacity][len(weights) - 1]


if __name__ == "__main__":
    print(knapsack_problem_rec([2, 3, 5, 7], [1, 3, 10, 2], 17))
    print(knapsack_mem([2, 3, 5, 7], [1, 3, 10, 2], 17))
