class Solution:
    def climbStairs(self, n: int) -> int:
        dp0, dp1 = 1, 1
        for _ in range(1, n):
            dp0, dp1 = dp1, dp0 + dp1
        return dp1
