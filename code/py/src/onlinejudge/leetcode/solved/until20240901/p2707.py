from onlinejudge.leetcode import *


class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        dictionary = set(dictionary)
        n = len(s)
        dp = [0] + [0] * n
        for hi in range(1, 1 + n):
            dp[hi] = min(dp[hi - 1] + 1, min((dp[lo] for lo in range(hi) if s[lo:hi] in dictionary), default=n))
        return dp[-1]
