from onlinejudge.leetcode import *


class Solution:
    def minimumCost(self, s: str) -> int:
        n = len(s)
        return sum(min(i, n - i) for i, (lst, nxt) in enumerate(pairwise(s), start=1) if lst != nxt)
