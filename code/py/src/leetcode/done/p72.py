class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        len1_word1, len1_word2 = 1 + len(word1), 1 + len(word2)
        dp = [[_i for _i in range(len1_word2)]] + [[_i] for _i in range(1, len1_word1)]
        for i in range(1, len1_word1):
            for j in range(1, len1_word2):
                dp[i].append(dp[i - 1][j - 1] if word1[i - 1] == word2[j - 1] else 1 + min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]))
        return dp[-1][-1]


sol = Solution()

eg_word1 = "horse"
eg_word2 = "ros"
print(sol.minDistance(word1 = eg_word1, word2 = eg_word2))
