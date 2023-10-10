from leetcode.util import *


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        dp = [[], [triangle[0][0]]]
        for i in range(1, len(triangle)):
            dp[0], dp[1] = dp[1], [triangle[i][0] + dp[1][0]]
            for j in range(1, i):
                dp[1].append(triangle[i][j] + min(dp[0][j - 1], dp[0][j]))
            dp[1].append(triangle[i][-1] + dp[0][-1])
        return min(dp[1])


sol = Solution()

triangle_ls = [[-1], [3, 2], [-3, 1, -1]]
print(sol.minimumTotal(triangle_ls))
