from leetcode.leetcode import *


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        first, second = 0, min(cost[0], cost[1])
        for i in range(2, len(cost)):
            first, second = second, min(second + cost[i], first + cost[i - 1])
        return second
