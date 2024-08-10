from onlinejudge.leetcode import *


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp0, dp1, dp2 = -prices.pop(0), 0, 0
        for price in prices:
            dp0, dp1, dp2 = max(dp0, dp2 - price), dp0 + price, max(dp1, dp2)
        return max(dp1, dp2)


sol = Solution()

eg_prices = [1, 2, 3, 0, 2]
print(sol.maxProfit(prices = eg_prices))
