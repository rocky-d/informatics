from leetcode.util import *


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        word_len_zip = tuple(zip(wordDict, [len(word) for word in wordDict]))
        lens = len(s)
        dp = [True] + [False for _ in range(lens)]
        for i in range(lens):
            if dp[i]:
                for word, len_word in word_len_zip:
                    if s[i:].startswith(word):
                        dp[i + len_word] = True
        return dp[-1]


sol = Solution()

eg_s = "applepenapple"
eg_wordDict = ["apple", "pen"]
print(sol.wordBreak(s = eg_s, wordDict = eg_wordDict))
