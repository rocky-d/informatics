from rockyutil.leetcode import *


class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        n = len(jobDifficulty)
        dp = [[-1 for _ in range(d)] for _ in range(n)]
        dp[0][0] = max(jobDifficulty[:1])
        for i in range(1, n):
            dp[i][0] = max(jobDifficulty[:i + 1])
            for j in range(min(i, d - 1), 0, -1):
                today = jobDifficulty[i]
                until_today = dp[i - 1][j - 1] + today
                for k in range(1, i - j + 1):
                    today = max(today, jobDifficulty[i - k])
                    until_today = min(until_today, dp[i - k - 1][j - 1] + today)
                dp[i][j] = until_today
        return dp[-1][-1]


eg_jobDifficulty = [6, 5, 4, 3, 2, 1]
eg_d = 4
print(Solution().minDifficulty(jobDifficulty = eg_jobDifficulty, d = eg_d))

#      j=0           j=1                                                           j=2
# i=0  max(6)        -1                                                            -1
# i=1  max(6,5)      min(dp[0][0]+max(5))                                          -1
# i=2  max(6,5,4)    min(dp[1][0]+max(4), dp[0][0]+max(5,4))                       min(dp[1][1]+max(4))
# i=3  max(6,5,4,3)  min(dp[2][0]+max(3), dp[1][0]+max(4,3), dp[0][0]+max(5,4,3))  min()
