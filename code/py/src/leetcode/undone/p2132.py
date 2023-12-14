from rockyutil.leetcode import *


class Solution:
    def possibleToStamp(self, grid: List[List[int]], stampHeight: int, stampWidth: int) -> bool:
        m, n = len(grid), len(grid[0])

        pre_sum = [[0 for _ in range(1 + n)] for _ in range(1 + m)]
        for i in range(m):
            for j in range(n):
                pre_sum[i + 1][j + 1] = grid[i][j] + pre_sum[i + 1][j] + pre_sum[i][j + 1] - pre_sum[i][j]

        diff = [[0 for _ in range(2 + n)] for _ in range(2 + m)]
        for i in range(m + 1 - stampHeight):
            for j in range(n + 1 - stampWidth):
                x = i + stampHeight
                y = j + stampWidth
                if pre_sum[x][y] - pre_sum[x][j] - pre_sum[i][y] + pre_sum[i][j] == 0:
                    diff[i + 1][j + 1] += 1
                    diff[x + 1][y + 1] += 1
                    diff[i + 1][y + 1] -= 1
                    diff[x + 1][j + 1] -= 1

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                diff[i][j] += diff[i - 1][j] + diff[i][j - 1] - diff[i - 1][j - 1]
                if diff[i][j] == 0 and grid[i - 1][j - 1] == 0:
                    return False
        return True
