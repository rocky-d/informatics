from onlinejudge.leetcode import *


class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        dictionary = set(dictionary)
        dp = [0]
        for i in range(1, 1 + len(s)):
            dp.append(dp[-1] + 1)
            for j in range(i):
                if s[j:i] in dictionary:
                    dp[-1] = min(dp[-1], dp[j])
        return dp[-1]
