from onlinejudge.leetcode import *


class Solution:
    def minSteps(self, n: int) -> int:
        dp = [-1, 0]
        for num in range(2, n + 1):
            dp.append(num)
            for factor in range(1, isqrt(num) + 1):
                if 0 == num % factor:
                    dp[num] = min(dp[num], dp[factor] + num // factor, dp[num // factor] + factor)
        return dp[-1]


eg_n = 18
print(Solution().minSteps(eg_n))
