from rockyutil.leetcode import *


class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        n = len(profit)
        jobs = sorted(zip(startTime, endTime, profit), key = lambda x: x[1])
        dp = [0 for _ in range(jobs[-1][1] + 1)]
        end = jobs[0][1]
        dp[end] = jobs[0][2]
        last_end = end
        for i in range(1, n):
            end = jobs[i][1]
            for j in range(last_end + 1, end + 1):
                dp[j] = dp[last_end]
            last_end = end
            dp[end] = max(dp[end], dp[jobs[i][0]] + jobs[i][2])
        return dp[-1]


eg_startTime = [1, 2, 3, 4, 6]
eg_endTime = [3, 5, 10, 6, 9]
eg_profit = [20, 20, 100, 70, 60]
print(Solution().jobScheduling(startTime = eg_startTime, endTime = eg_endTime, profit = eg_profit))
