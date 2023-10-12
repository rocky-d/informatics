from leetcode.util import *


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        dp = [list(map(int, matrix[0]))]
        for i in range(1, len(matrix)):
            dp.append([int(matrix[i][0])])
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                for k in range(1 + dp[i - 1][j - 1]):
                    if '0' == matrix[i - k][j] or '0' == matrix[i][j - k]:
                        dp[i].append(k)
                        break
                else:
                    dp[i].append(1 + dp[i - 1][j - 1])
        return max([max(row) for row in dp]) ** 2


sol = Solution()

example_matrix = [
    ["1", "0", "1", "0", "0"],
    ["1", "0", "1", "1", "1"],
    ["1", "1", "1", "1", "1"],
    ["1", "0", "0", "1", "0"]
]
print(sol.maximalSquare(example_matrix))
