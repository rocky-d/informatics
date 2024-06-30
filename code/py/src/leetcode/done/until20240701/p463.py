from rockyutil.leetcode import *


class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        ans = 0
        m, n = len(grid), len(grid[0])
        for row in grid:
            idx = 0
            while idx < n:
                while idx < n and 0 == row[idx]:
                    idx += 1
                island = False
                while idx < n and 1 == row[idx]:
                    island = True
                    idx += 1
                if island:
                    ans += 2
        for col in ([row[i] for row in grid] for i in range(n)):
            idx = 0
            while idx < m:
                while idx < m and 0 == col[idx]:
                    idx += 1
                island = False
                while idx < m and 1 == col[idx]:
                    island = True
                    idx += 1
                if island:
                    ans += 2
        return ans
