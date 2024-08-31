from onlinejudge.leetcode import *


class Solution:
    def possibleToStamp(self, grid: List[List[int]], stampHeight: int, stampWidth: int) -> bool:
        m, n = len(grid), len(grid[0])
        prefs = [[0] + [0 for _ in range(n)]] + [[0] for _ in range(m)]
        for i, row in enumerate(grid, 1):
            for j, val in enumerate(row, 1):
                prefs[i].append(val - prefs[i - 1][j - 1] + prefs[i - 1][j] + prefs[i][j - 1])
        diffs = [[0 for _ in range(n)] for _ in range(m)]
        for x1 in range(m - stampHeight + 1):
            x2 = x1 + stampHeight
            for y1 in range(n - stampWidth + 1):
                y2 = y1 + stampWidth
                if 0 == prefs[x2][y2] + prefs[x1][y1] - prefs[x1][y2] - prefs[x2][y1]:
                    diffs[x1][y1] += 1
                    if x2 < m and y2 < n:
                        diffs[x2][y2] += 1
                    if x2 < m:
                        diffs[x2][y1] -= 1
                    if y2 < n:
                        diffs[x1][y2] -= 1
        cover = [[0] + [0 for _ in range(n)]] + [[0] for _ in range(m)]
        for i, row in enumerate(diffs, 1):
            for j, val in enumerate(row, 1):
                cover[i].append(val - cover[i - 1][j - 1] + cover[i - 1][j] + cover[i][j - 1])
                grid[i - 1][j - 1] += cover[i][j]
        return all(all(0 < val for val in row) for row in grid)


eg_grid = [
    [1, 0, 0, 0],
    [1, 0, 0, 0],
    [1, 0, 0, 0],
    [1, 0, 0, 0],
    [1, 0, 0, 0],
]
eg_stampHeight = 4
eg_stampWidth = 3
print(Solution().possibleToStamp(eg_grid, eg_stampHeight, eg_stampWidth))
