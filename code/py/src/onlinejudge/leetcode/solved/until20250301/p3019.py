from onlinejudge.leetcode import *


class Solution:
    def countKeyChanges(self, s: str) -> int:
        return sum(1 for lst, nxt in pairwise(s.upper()) if lst != nxt)
