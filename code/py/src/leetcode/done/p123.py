from rockyutil.leetcode import *


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        NEGATIVE_INFINITY = -10000000000
        dp = [0, NEGATIVE_INFINITY, NEGATIVE_INFINITY, NEGATIVE_INFINITY, NEGATIVE_INFINITY]
        for price in prices:
            dp[1], dp[2], dp[3], dp[4] = max(-price, dp[1]), max(dp[1] + price, dp[2]), max(dp[2] - price, dp[3]), max(dp[3] + price, dp[4])
        return max(dp)


sol = Solution()

eg_prices = [3, 3, 5, 0, 0, 3, 1, 4]
print(sol.maxProfit(prices = eg_prices))
