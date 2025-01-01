from onlinejudge.leetcode import *


class Solution:
    def twoEggDrop(self, n: int) -> int:
        return ceil((sqrt(n * 8 + 1) - 1) / 2)
