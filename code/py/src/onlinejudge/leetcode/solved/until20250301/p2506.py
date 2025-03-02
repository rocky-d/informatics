from onlinejudge.leetcode import *


class Solution:
    def similarPairs(self, words: List[str]) -> int:
        ans = 0
        n = len(words)
        for i in range(n):
            chars = frozenset(words[i])
            for j in range(i + 1, n):
                if chars == frozenset(words[j]):
                    ans += 1
        return ans
