class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp = [[_i for _i in range(1 + len(word2))]] + [[_i] for _i in range(1, 1 + len(word1))]
        for i, ch1 in enumerate(word1):
            i1 = i + 1
            for j, ch2 in enumerate(word2):
                dp[i1].append(dp[i][j] if ch1 == ch2 else 1 + min(dp[i][j], dp[i1][j], dp[i][j + 1]))
        return dp[-1][-1]


sol = Solution()

eg_word1 = "horse"
eg_word2 = "ros"
print(sol.minDistance(word1 = eg_word1, word2 = eg_word2))
