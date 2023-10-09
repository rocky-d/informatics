from leetcode.util import *


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        m_1 = m - 1
        n_1 = n - 1
        dp = [[0 for __ in range(n_1)] for _ in range(m_1)] + [[]]
        for i in range(n_1, -1, -1):
            if 0 == obstacleGrid[-1][i]:
                dp[-1].insert(0, 1)
            else:
                dp[-1] = [0 for _ in range(i + 1)] + dp[-1]
                break
        dp[-1].pop(-1)
        for i in range(m_1, -1, -1):
            if 0 == obstacleGrid[i][-1]:
                dp[i].append(1)
            else:
                for ii in range(i, -1, -1):
                    dp[ii].append(0)
                break
        for i in range(m - 2, -1, -1):
            for j in range(n - 2, -1, -1):
                if 0 == obstacleGrid[i][j]:
                    if 0 == obstacleGrid[i + 1][j]:
                        dp[i][j] += dp[i + 1][j]
                    if 0 == obstacleGrid[i][j + 1]:
                        dp[i][j] += dp[i][j + 1]
        return dp[0][0]


sol = Solution()

print(sol.uniquePathsWithObstacles([[1, 0], [0, 0]]))
