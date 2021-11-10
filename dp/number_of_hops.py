import sys


def count_hops_rec(distance, hops):
    if distance < 0:
        return 0
    if distance == 0:
        return 1
    return sum(count_hops_rec(distance - h, hops) for h in hops)


def count_hops_mem(distance, hops):
    dp = [0 for _ in range(distance + 1)]
    dp[0] = 1
    for i in range(1, distance + 1):
        for h in hops:
            if i - h >= 0:
                dp[i] += dp[i - h]
    return dp[distance]


if __name__ == "__main__":
    print(count_hops_rec(5, [1, 2, 3]))
    print(count_hops_mem(5, [1, 2, 3]))
