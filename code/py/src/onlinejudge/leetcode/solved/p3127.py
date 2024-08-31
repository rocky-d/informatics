from onlinejudge.leetcode import *


class Solution:
    def canMakeSquare(self, grid: List[List[str]]) -> bool:
        return any(2 != sum(1 for dx, dy in product(range(2), range(2)) if 'W' == grid[x + dx][y + dy]) for x, y in product(range(2), range(2)))
