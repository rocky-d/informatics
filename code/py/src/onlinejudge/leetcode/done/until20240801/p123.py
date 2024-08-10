from onlinejudge.leetcode import *


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        NEGATIVE_INFINITY = -10000000000
        dp = [[0, NEGATIVE_INFINITY, NEGATIVE_INFINITY], [NEGATIVE_INFINITY, NEGATIVE_INFINITY]]
        for price in prices:
            dp[0][2], dp[1][1], dp[0][1], dp[1][0] = max(dp[0][2], dp[1][1] + price), max(dp[1][1], dp[0][1] - price), max(dp[0][1], dp[1][0] + price), max(dp[1][0], dp[0][0] - price)
        return max(dp[0])


sol = Solution()

eg_prices = [3, 3, 5, 0, 0, 3, 1, 4]
print(sol.maxProfit(prices = eg_prices))
