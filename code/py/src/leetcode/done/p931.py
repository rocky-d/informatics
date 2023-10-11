from leetcode.util import *


class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        n_1 = n - 1
        first, second = [], matrix[0]
        for i in range(1, n):
            first, second = second, [matrix[i][0] + min(second[0], second[1])]
            for j in range(1, n_1):
                second.append(matrix[i][j] + min(first[j - 1], first[j], first[j + 1]))
            second.append(matrix[i][-1] + min(first[-2], first[-1]))
        return min(second)


sol = Solution()

example_matrix = [[2, 1, 3], [6, 5, 4], [7, 8, 9]]
print(sol.minFallingPathSum(example_matrix))
