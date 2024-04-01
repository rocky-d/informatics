from rockyutil.leetcode import *


class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        dp0, dp1 = [], matrix[0]
        for i in range(1, n):
            dp0, dp1 = dp1, [matrix[i][0] + min(dp1[0], dp1[1])]
            for j in range(1, n - 1):
                dp1.append(matrix[i][j] + min(dp0[j - 1], dp0[j], dp0[j + 1]))
            dp1.append(matrix[i][-1] + min(dp0[-2], dp0[-1]))
        return min(dp1)


eg_matrix = [
    [2, 1, 3],
    [6, 5, 4],
    [7, 8, 9]
]
print(Solution().minFallingPathSum(matrix = eg_matrix))
