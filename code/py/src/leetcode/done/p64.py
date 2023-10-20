from leetcode.leetcode import *


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        dp = [grid[0][0]]
        tmp_val = dp[0]
        for i in range(1, n):
            tmp_val += grid[0][i]
            dp.append(tmp_val)
        for i in range(1, m):
            dp[0] += grid[i][0]
            for j in range(1, n):
                dp[j] = grid[i][j] + min(dp[j], dp[j - 1])
        return dp[-1]


sol = Solution()

print(sol.minPathSum([[1, 3, 1], [1, 5, 1], [4, 2, 1]]))
