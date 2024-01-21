class Solution:
    def climbStairs(self, n: int) -> int:
        dp0, dp1 = 1, 2
        for _i in range(2, n):
            dp0, dp1 = dp1, dp0 + dp1
        return 1 if 1 == n else dp1
