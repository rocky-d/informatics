from rockyutil.leetcode import *


class Solution:
    def numberOfRightTriangles(self, grid: List[List[int]]) -> int:
        a, b = [0] * len(grid), [0] * len(grid[0])
        for i, row in enumerate(grid):
            for j, val in enumerate(row):
                if 1 == val:
                    a[i] += 1
                    b[j] += 1
        return sum((a[i] - 1) * (b[j] - 1) for i, row in enumerate(grid) for j, val in enumerate(row) if 1 == val)
