from onlinejudge.leetcode import *


class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        cnter = [-1] + [0] * (n * n)
        for i in range(n):
            for j in range(n):
                cnter[grid[i][j]] += 1
        return [cnter.index(2), cnter.index(0)]
