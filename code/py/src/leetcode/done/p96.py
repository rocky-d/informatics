class Solution:
    def numTrees(self, n: int) -> int:
        dp = [0, 1]
        for i in range(2, n + 1):
            dp.append(2 * dp[-1])
            for j in range(2, i):
                dp[-1] += dp[j - 1] * dp[i - j]
        return dp[-1]


sol = Solution()

eg_n = 5
print(sol.numTrees(n = eg_n))
