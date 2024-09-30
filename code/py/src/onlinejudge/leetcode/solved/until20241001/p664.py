class Solution:
    def strangePrinter(self, s: str) -> int:
        n = len(s)
        dp = [[0] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = 1
        for diff in range(1, n):
            for lft, rit in zip(range(0, n - diff), range(diff, n)):
                dp[lft][rit] = dp[lft + 1][rit] if s[lft] == s[rit] else min(dp[lft][i] + dp[i + 1][rit] for i in range(lft, rit))
        return dp[0][-1]
