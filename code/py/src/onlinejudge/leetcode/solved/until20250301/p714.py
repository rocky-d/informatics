from onlinejudge.leetcode import *


class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        dp0, dp1 = -prices.pop(0), 0
        for price in prices:
            dp0, dp1 = max(dp0, dp1 - price), max(dp0 + price - fee, dp1)
        return dp1
