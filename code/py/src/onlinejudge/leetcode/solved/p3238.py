from onlinejudge.leetcode import *


class Solution:
    def winningPlayerCount(self, n: int, pick: List[List[int]]) -> int:
        cnter = [[0] * 11 for _ in range(n)]
        for x, y in pick:
            cnter[x][y] += 1
        return sum(1 for i, ls in enumerate(cnter) if i < max(ls))
