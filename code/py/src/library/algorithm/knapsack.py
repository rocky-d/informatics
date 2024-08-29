from itertools import groupby


def knapsack_01(items, volume):
    dp = [0] + [0] * volume
    for weight, value in items:
        for vol in reversed(range(weight, volume + 1)):
            dp[vol] = max(dp[vol], dp[vol - weight] + value)
    return dp[-1]


def knapsack_bounded(items, volume):
    dp = [0] + [0] * volume
    for (weight, value), group in groupby(items):
        weights = len(list(group)) * weight
        if weights < volume:
            for vol in reversed(range(volume + 1)):
                times = min(weights, vol) // weight
                for w, v in zip(
                    range(weight, weight * times + 1, weight),
                    range(value, value * times + 1, value),
                ):
                    dp[vol] = max(dp[vol], dp[vol - w] + v)
        else:  # elif weights >= volume:
            for vol in range(weight, volume + 1):
                dp[vol] = max(dp[vol], dp[vol - weight] + value)
    return dp[-1]


def knapsack_unbounded(items, volume):
    dp = [0] + [0] * volume
    for weight, value in items:
        for vol in range(weight, volume + 1):
            dp[vol] = max(dp[vol], dp[vol - weight] + value)
    return dp[-1]


if __name__ == '__main__':
    items, volume = sorted([(1, 2), (1, 2), (2, 3), (3, 5), (4, 7)]), 6
    print(knapsack_01(items, volume))
    print(knapsack_bounded(items, volume))
    print(knapsack_unbounded(items, volume))
