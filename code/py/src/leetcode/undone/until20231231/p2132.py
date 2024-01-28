from rockyutil.leetcode import *


class Solution:
    def possibleToStamp(self, grid: List[List[int]], stampHeight: int, stampWidth: int) -> bool:
        m, n = len(grid), len(grid[0])

        pre = [[0 for _ in range(1 + n)] for _ in range(1 + m)]
        for i in range(m):
            for j in range(n):
                pre[i + 1][j + 1] = grid[i][j] + pre[i + 1][j] + pre[i][j + 1] - pre[i][j]

        diff = [[0 for _ in range(2 + n)] for _ in range(2 + m)]
        for i in range(m - stampHeight + 1):
            for j in range(n - stampWidth + 1):
                x = i + stampHeight
                y = j + stampWidth
                if 0 == pre[x][y] - pre[x][j] - pre[i][y] + pre[i][j]:
                    diff[i + 1][j + 1] += 1
                    diff[x + 1][y + 1] += 1
                    diff[i + 1][y + 1] -= 1
                    diff[x + 1][j + 1] -= 1

        for i in range(m):
            for j in range(n):
                diff[i + 1][j + 1] += diff[i][j + 1] + diff[i + 1][j] - diff[i][j]
                if 0 == grid[i][j] and 0 == diff[i + 1][j + 1]:
                    return False
        return True
