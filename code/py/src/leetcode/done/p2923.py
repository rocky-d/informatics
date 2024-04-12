from rockyutil.leetcode import *


class Solution:
    def findChampion(self, grid: List[List[int]]) -> int:
        n = len(grid)
        for i, row in enumerate(grid):
            if n - 1 == row.count(1):
                ans = i
                break
        else:
            ans = -1
        return ans
