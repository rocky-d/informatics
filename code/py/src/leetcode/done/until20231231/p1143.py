class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp0, dp1 = [0] + [0 for _ in text2], [0] + [0 for _ in text2]
        for char1 in text1:
            for j, char2 in enumerate(text2):
                dp1[j + 1] = dp0[j] + 1 if char1 == char2 else max(dp0[j + 1], dp1[j])
            dp0, dp1 = dp1, dp0
        return dp0[-1]


eg_text1 = 'abcde'
eg_text2 = 'ace'
print(Solution().longestCommonSubsequence(text1 = eg_text1, text2 = eg_text2))
