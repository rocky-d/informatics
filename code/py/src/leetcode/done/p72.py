class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        len_word1, len_word2 = len(word1), len(word2)
        dp = [[_i for _i in range(1 + len_word2)]] + [[_i] for _i in range(1, 1 + len_word1)]
        for i in range(len_word1):
            for j in range(len_word2):
                dp[i + 1].append(dp[i][j] if word1[i] == word2[j] else 1 + min(dp[i][j], dp[i + 1][j], dp[i][j + 1]))
        return dp[-1][-1]


sol = Solution()

eg_word1 = "horse"
eg_word2 = "ros"
print(sol.minDistance(word1 = eg_word1, word2 = eg_word2))
