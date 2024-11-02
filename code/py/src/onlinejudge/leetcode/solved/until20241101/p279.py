from onlinejudge.leetcode import *


class Solution:
    def numSquares(self, n: int) -> int:
        dp = [i for i in range(1 + n)]
        for i in (i * i for i in range(isqrt(n), 1, -1)):
            for j in range(i, 1 + n):
                dp[j] = min(dp[j], 1 + dp[j - i])
        return dp[-1]


eg_n = 13
print(Solution().numSquares(eg_n))
