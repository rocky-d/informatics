from rockyutil.leetcode import *


class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        dp0, dp1 = -prices.pop(0), 0
        for price in prices:
            new_dp0, new_dp1 = max(dp0, dp1 - price), max(dp0 + price - fee, dp1)
            dp0, dp1 = new_dp0, new_dp1
        return dp1
