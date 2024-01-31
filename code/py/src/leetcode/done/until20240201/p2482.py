from rockyutil.leetcode import *


class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        onesRow, onesCol = [0 for _ in range(m)], [0 for _ in range(n)]
        zerosRow, zerosCol = [0 for _ in range(m)], [0 for _ in range(n)]
        for i in range(m):
            for j in range(n):
                if 0 == grid[i][j]:
                    zerosRow[i] += 1
                    zerosCol[j] += 1
                else:  # elif 1 == grid[i][j]:
                    onesRow[i] += 1
                    onesCol[j] += 1
        diff = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                diff[i][j] = onesRow[i] + onesCol[j] - zerosRow[i] - zerosCol[j]
        return diff
