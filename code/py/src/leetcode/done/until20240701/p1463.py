from rockyutil.leetcode import *


class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = {(0, n - 1): grid[0][0] + grid[0][-1]}
        for row in range(1, m):
            dp_lst, dp = dp, defaultdict(lambda: -1)
            for (a, b), val in dp_lst.items():
                for x, y in (-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 0), (0, 1), (1, -1), (1, 0), (1, 1):
                    ax, by = a + x, b + y
                    if 0 <= ax < n and 0 <= by < n:
                        dp[ax, by] = max(dp[ax, by], dp_lst[a, b] + (grid[row][ax] if ax == by else grid[row][ax] + grid[row][by]))
        return max(dp.values())


eg_grid = [
    [1, 0, 0, 3],
    [0, 0, 0, 3],
    [0, 0, 3, 3],
    [9, 0, 3, 3],
]
print(Solution().cherryPickup(eg_grid))
