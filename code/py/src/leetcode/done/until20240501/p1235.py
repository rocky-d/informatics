from rockyutil.leetcode import *


class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        jobs = sorted(zip(startTime, endTime, profit), key = lambda x: x[1])
        dp = [0]
        for i, job in enumerate(jobs):
            dp.append(max(dp[i], dp[bisect_right(jobs, job[0], key = lambda x: x[1])] + job[2]))
        return dp[-1]


eg_startTime = [1, 2, 3, 4, 6]
eg_endTime = [3, 5, 10, 6, 9]
eg_profit = [20, 20, 100, 70, 60]
print(Solution().jobScheduling(startTime = eg_startTime, endTime = eg_endTime, profit = eg_profit))
