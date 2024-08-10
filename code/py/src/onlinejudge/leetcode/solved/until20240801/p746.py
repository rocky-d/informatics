from onlinejudge.leetcode import *


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = 0, 0
        for cost_i in cost:
            dp = min(dp) + cost_i, dp[0]
        return min(dp)
