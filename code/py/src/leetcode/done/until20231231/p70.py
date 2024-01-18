class Solution:
    def climbStairs(self, n: int) -> int:
        dp = 1, 2
        for _i in range(2, n):
            dp = dp[1], dp[0] + dp[1]
        return 1 if 1 == n else dp[-1]
