from onlinejudge.leetcode import *


class Solution:
    def maxScore(self, grid: List[List[int]]) -> int:
        ans = -100_000
        m, n = len(grid), len(grid[0])
        dp = [[0] * n for _ in range(m)]
        range_row, range_col = range(m - 2, -1, -1), range(n - 2, -1, -1)
        for row in range_row:
            dp[row][-1] = grid[row + 1][-1] - grid[row][-1]
        for col in range_col:
            dp[-1][col] = grid[-1][col + 1] - grid[-1][col]
        for row in range_row:
            for col in range_col:
                dp[row][col] = max(
                    grid[row + 1][col] - grid[row][col],
                    grid[row][col + 1] - grid[row][col],
                )
        for row in range_row:
            res = dp[row][-1] = max(dp[row][-1], grid[row + 1][-1] - grid[row][-1] + dp[row + 1][-1])
            ans = max(ans, res)
        for col in range_col:
            res = dp[-1][col] = max(dp[-1][col], grid[-1][col + 1] - grid[-1][col] + dp[-1][col + 1])
            ans = max(ans, res)
        for row in range_row:
            for col in range_col:
                res = dp[row][col] = max(
                    dp[row][col],
                    grid[row + 1][col] - grid[row][col] + dp[row + 1][col],
                    grid[row][col + 1] - grid[row][col] + dp[row][col + 1],
                )
                ans = max(ans, res)
        return ans
