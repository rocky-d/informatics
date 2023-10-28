class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[0 for _j in range(1 + len(text2))] for _i in range(1 + len(text1))]
        for i, text1_i in enumerate(text1):
            for j, text2_j in enumerate(text2):
                dp[i + 1][j + 1] = dp[i][j] + 1 if text1_i == text2_j else max(dp[i][j + 1], dp[i + 1][j])
        return dp[-1][-1]


sol = Solution()

eg_text1 = "abcde"
eg_text2 = "ace"
print(sol.longestCommonSubsequence(text1 = eg_text1, text2 = eg_text2))
