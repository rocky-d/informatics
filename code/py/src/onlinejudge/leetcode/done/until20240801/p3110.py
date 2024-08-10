from onlinejudge.leetcode import *


class Solution:
    def scoreOfString(self, s: str) -> int:
        return sum(abs(lst - nxt) for lst, nxt in pairwise(map(ord, s)))
