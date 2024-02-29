from rockyutil.leetcode import *


class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        cost1, cost7, cost30 = costs
        dp = [0]
        for day in days:
            while len(dp) < day:
                dp.append(dp[-1])
            dp.append(min(dp[max(0, day - 1)] + cost1, dp[max(0, day - 7)] + cost7, dp[max(0, day - 30)] + cost30))
        return dp[-1]


eg_days = [1, 4, 6, 7, 8, 20]
eg_costs = [2, 7, 15]
print(Solution().mincostTickets(eg_days, eg_costs))
