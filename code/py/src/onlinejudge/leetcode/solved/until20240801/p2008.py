from onlinejudge.leetcode import *


class Solution:
    def maxTaxiEarnings(self, n: int, rides: List[List[int]]) -> int:
        rides.sort(key = lambda x: x[1])
        j = 0
        dp = [0 for _i in range(1 + n)]
        for i in range(1, 1 + n):
            dp[i] = max(dp[i], dp[i - 1])
            while j < len(rides):
                if i < rides[j][1]:
                    break
                else:
                    dp[i] = max(dp[i], dp[rides[j][0]] - rides[j][0] + rides[j][1] + rides[j][2])
                    j += 1
        return dp[-1]


sol = Solution()

eg_n = 20
eg_rides = [[1, 6, 1], [3, 10, 2], [10, 12, 3], [11, 12, 2], [12, 15, 2], [13, 18, 1]]
print(sol.maxTaxiEarnings(n = eg_n, rides = eg_rides))
