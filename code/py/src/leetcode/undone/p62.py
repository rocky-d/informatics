class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        m_1 = m - 1
        n_1 = n - 1
        dp = [[1 for _ in range(n)]] + [[1] + [0 for __ in range(n_1)] for _ in range(m_1)]
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[-1][-1]


sol = Solution()
print(sol.uniquePaths(3, 7))
