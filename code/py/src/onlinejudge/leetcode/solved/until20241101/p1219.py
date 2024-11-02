from onlinejudge.leetcode import *


class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        def dfs(x: int, y: int) -> int:
            if 0 == grid[x][y]:
                return 0
            val, grid[x][y] = grid[x][y], 0
            res = val + max(dfs(x_nxt, y_nxt) for x_nxt, y_nxt in ((x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)) if 0 <= x_nxt < m and 0 <= y_nxt < n)
            grid[x][y] = val
            return res

        return max(dfs(x = i, y = j) for i in range(m) for j in range(n))
