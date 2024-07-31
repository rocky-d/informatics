from rockyutil.leetcode import *


class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        return [[max(grid[x][y] for x in range(i, i + 3) for y in range(j, j + 3)) for j in range(n - 2)] for i in range(n - 2)]
