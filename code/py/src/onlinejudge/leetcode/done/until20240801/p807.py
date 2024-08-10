from onlinejudge.leetcode import *


class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        n = len(grid)
        row_maxms, col_maxms = tuple(max(row[c] for c in range(n)) for row in grid), tuple(max(row[c] for row in grid) for c in range(n))
        return sum(min(row_maxms[r], col_maxms[c]) - val for r, row in enumerate(grid) for c, val in enumerate(row))
