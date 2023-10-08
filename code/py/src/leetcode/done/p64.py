from leetcode.util import *


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        m_1 = m - 1
        n_1 = n - 1
        dp = [[0 for __ in range(n_1)] for _ in range(m_1)]
        dp.insert(0, [grid[0][0]])
        tmp_val = dp[0][0]
        for i in range(1, m):
            tmp_val += grid[i][0]
            dp[i].insert(0, tmp_val)
        tmp_val = dp[0][0]
        for i in range(1, n):
            tmp_val += grid[0][i]
            dp[0].append(tmp_val)
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = grid[i][j] + min(dp[i - 1][j], dp[i][j - 1])
        return dp[-1][-1]


sol = Solution()

print(sol.minPathSum([[1, 3, 1], [1, 5, 1], [4, 2, 1]]))
