from rockyutil.leetcode import *


class Solution:
    def possibleToStamp(self, grid: List[List[int]], stampHeight: int, stampWidth: int) -> bool:
        m, n = len(grid), len(grid[0])
        prefs = [[0] + [0 for _ in range(n)]] + [[0] for _ in range(m)]
        for i, row in enumerate(grid, 1):
            for j, val in enumerate(row, 1):
                prefs[i].append(val - prefs[i - 1][j - 1] + prefs[i - 1][j] + prefs[i][j - 1])
        diffs = [[0 for _ in range(2 + n)] for _ in range(2 + m)]
        for x1 in range(m - stampHeight + 1):
            for y1 in range(n - stampWidth + 1):
                x2, y2 = x1 + stampHeight, y1 + stampWidth
                if 0 == prefs[x2][y2] + prefs[x1][y1] - prefs[x1][y2] - prefs[x2][y1]:
                    diffs[x2 + 1][y2 + 1] += 1
                    diffs[x1 + 1][y1 + 1] += 1
                    diffs[x1 + 1][y2 + 1] -= 1
                    diffs[x2 + 1][y1 + 1] -= 1
        for i in range(m):
            for j in range(n):
                diffs[i + 1][j + 1] += diffs[i][j + 1] + diffs[i + 1][j] - diffs[i][j]
                if 0 == grid[i][j] and 0 == diffs[i + 1][j + 1]:
                    ans = False
                    break
            else:
                continue
            break
        else:
            ans = True
        return ans
