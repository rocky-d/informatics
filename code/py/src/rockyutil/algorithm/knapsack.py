def knapsack_01(items, volume):
    dp = [0] * (1 + volume)
    for weight, value in items:
        for vol in range(volume, weight - 1, -1):
            dp[vol] = max(dp[vol], dp[vol - weight] + value)
    return dp[-1]


def knapsack_unbounded(items, volume):
    dp = [0] * (1 + volume)
    for weight, value in items:
        for vol in range(weight, volume + 1):
            dp[vol] = max(dp[vol], dp[vol - weight] + value)
    return dp[-1]


if __name__ == '__main__':
    items, volume = [(1, 2), (2, 3), (3, 5), (4, 7)], 6
    print(knapsack_01(items, volume))
    print(knapsack_unbounded(items, volume))
