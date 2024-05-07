from rockyutil.leetcode import *


class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = {(0, n - 1): grid[0][0] + grid[0][-1]}
        for i in range(1, m):
            dp_lst, dp = dp, defaultdict(lambda: -1)
            for (j, k), val in dp_lst.items():
                for x, y in (-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 0), (0, 1), (1, -1), (1, 0), (1, 1):
                    jx, ky = j + x, k + y
                    if 0 <= jx < n and 0 <= ky < n:
                        dp[jx, ky] = max(dp[jx, ky], dp_lst[j, k] + (grid[i][jx] if jx == ky else grid[i][jx] + grid[i][ky]))
        return max(dp.values())


eg_grid = [
    [1, 0, 0, 3],
    [0, 0, 0, 3],
    [0, 0, 3, 3],
    [9, 0, 3, 3],
]
print(Solution().cherryPickup(eg_grid))
