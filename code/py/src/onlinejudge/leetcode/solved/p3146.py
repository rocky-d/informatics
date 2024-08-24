from onlinejudge.leetcode import *


class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        s_idxes = {}
        for idx, char in enumerate(s):
            s_idxes[char] = idx
        return sum(abs(s_idxes[char] - idx) for idx, char in enumerate(t))
