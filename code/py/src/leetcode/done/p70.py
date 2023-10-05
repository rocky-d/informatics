class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0, 1, 2]
        for _ in range(n - 2):
            dp.append(dp[-1] + dp[-2])
        return dp[n]
