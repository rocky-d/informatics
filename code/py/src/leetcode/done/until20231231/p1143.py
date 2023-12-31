class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp1, dp2 = [0] + [0 for _ in text2], [0] + [0 for _ in text2]
        for text1_i in text1:
            for j, text2_j in enumerate(text2):
                dp2[j + 1] = dp1[j] + 1 if text1_i == text2_j else max(dp1[j + 1], dp2[j])
            dp1, dp2 = dp2, dp1
        return dp1[-1]


sol = Solution()

eg_text1 = "abcde"
eg_text2 = "ace"
print(sol.longestCommonSubsequence(text1 = eg_text1, text2 = eg_text2))
