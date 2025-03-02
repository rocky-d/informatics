from onlinejudge.leetcode import *


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [0] + [inf for _ in range(amount)]
        for coin in coins:
            for vol in range(coin, amount + 1):
                dp[vol] = min(dp[vol], dp[vol - coin] + 1)
        return -1 if isinf(dp[-1]) else dp[-1]
