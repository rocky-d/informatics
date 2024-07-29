def knapsack_01(volume, items):
    dp = [0] * (1 + volume)
    for weight, value in items:
        for vol in range(volume, weight - 1, -1):
            dp[vol] = max(dp[vol], dp[vol - weight] + value)
    return dp[-1]


def knapsack_unbounded(volume, items):
    dp = [0] * (1 + volume)
    for weight, value in items:
        for vol in range(weight, volume + 1):
            dp[vol] = max(dp[vol], dp[vol - weight] + value)
    return dp[-1]


if __name__ == '__main__':
    ...
