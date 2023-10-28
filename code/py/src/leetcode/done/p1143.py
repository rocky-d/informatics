class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        len_text1, len_text2 = len(text1), len(text2)
        dp = [[0 for _j in range(1 + len_text2)] for _i in range(1 + len_text1)]
        for i in range(len_text1):
            for j in range(len_text2):
                if text1[i] == text2[j]:
                    dp[i + 1][j + 1] = dp[i][j] + 1
                else:
                    dp[i + 1][j + 1] = max(dp[i][j + 1], dp[i + 1][j])
        return dp[-1][-1]


sol = Solution()

eg_text1 = "abcde"
eg_text2 = "ace"
print(sol.longestCommonSubsequence(text1 = eg_text1, text2 = eg_text2))
