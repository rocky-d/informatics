from rockyutil.leetcode import *


class Solution:
    def findColumnWidth(self, grid: List[List[int]]) -> List[int]:
        return [max(len(str(grid[row][col])) for row in range(len(grid))) for col in range(len(grid[0]))]
