from onlinejudge.leetcode import *


class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        NEGATIVE_INFINITY = -1000000
        dp = [[0] + [NEGATIVE_INFINITY for _i in range(k)], [NEGATIVE_INFINITY for _i in range(k)]]
        for price in prices:
            for i in range(k, 0, -1):
                i_1 = i - 1
                dp[0][i], dp[1][i_1] = max(dp[0][i], dp[1][i_1] + price), max(dp[1][i_1], dp[0][i_1] - price)
        return max(dp[0])
