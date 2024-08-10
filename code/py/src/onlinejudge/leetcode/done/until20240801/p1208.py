from onlinejudge.leetcode import *


class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        prefs = list(accumulate((abs(ord(char1) - ord(char2)) for char1, char2 in zip(s, t)), initial = 0))
        return max(i - bisect_left(prefs, prefs[i] - maxCost) for i in range(1, len(s) + 1))
