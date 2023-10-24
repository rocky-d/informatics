from rockyutil.leetcode import *


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp0, dp1, dp2 = -prices[0], 0, 0
        for i in range(1, len(prices)):
            new_dp0 = max(dp0, dp2 - prices[i])
            new_dp1 = dp0 + prices[i]
            new_dp2 = max(dp1, dp2)
            dp0, dp1, dp2 = new_dp0, new_dp1, new_dp2
        return max(dp1, dp2)


sol = Solution()

eg_prices = [1, 2, 3, 0, 2]
print(sol.maxProfit(prices = eg_prices))
