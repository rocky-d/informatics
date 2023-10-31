class Solution:
    def numTrees(self, n: int) -> int:
        dp = [1, 1] + [0 for _i in range(n - 1)]
        for i in range(2, n + 1):
            for j in range(i):
                dp[i] += dp[j] * dp[i - j - 1]
        return dp[-1]


sol = Solution()

eg_n = 5
print(sol.numTrees(n = eg_n))
