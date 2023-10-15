class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        lens = len(s)
        dp = [[0 for _j in range(lens)] for _i in range(lens)]
        for right in range(lens):
            dp[right][right] = 1
            for left in range(right - 1, -1, -1):
                if s[right] == s[left]:
                    dp[left][right] = 2 + dp[left + 1][right - 1]
                else:
                    dp[left][right] = max(dp[left + 1][right], dp[left][right - 1])
        return dp[0][-1]


sol = Solution()

eg_s = "bbbab"
print(sol.longestPalindromeSubseq(s = eg_s))
