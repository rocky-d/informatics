from rockyutil.leetcode import *


class Solution:
    def findColumnWidth(self, grid: List[List[int]]) -> List[int]:
        ans = [0] * len(grid[0])
        for row in grid:
            for i, val in enumerate(row):
                ans[i] = max(ans[i], len(str(val)))
        return ans
