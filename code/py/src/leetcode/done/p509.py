class Solution:
    def fib(self, n: int) -> int:
        dp = [0, 1]
        for _ in range(n - 1):
            dp.append(dp[-1] + dp[-2])
        return dp[n]
