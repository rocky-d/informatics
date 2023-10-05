from leetcode.util import *


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [0, min(cost[0], cost[1])]
        for i in range(2, len(cost)):
            dp.append(min(dp[-1] + cost[i], dp[-2] + cost[i - 1]))
        return dp[-1]
