class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        lent = len(t)
        dp = [[1] + [0 for _j in range(lent)] for _i in range(1 + len(s))]
        for i, s_i in enumerate(s):
            i1 = i + 1
            for j, t_j in enumerate(t[: min(lent, i1)]):
                j1 = j + 1
                dp[i1][j1] = dp[i][j] + dp[i][j1] if s_i == t_j else dp[i][j1]
        return dp[-1][-1]


sol = Solution()

eg_s = "rabbbit"
eg_t = "rabbit"
print(sol.numDistinct(s = eg_s, t = eg_t))
