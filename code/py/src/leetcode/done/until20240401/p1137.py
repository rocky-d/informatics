class Solution:
    def tribonacci(self, n: int) -> int:
        dp0, dp1, dp2 = 0, 1, 1
        for _ in range(3, n + 1):
            dp0, dp1, dp2 = dp1, dp2, dp0 + dp1 + dp2
        return n if n < 2 else dp2
