from leetcode.leetcode import *


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m, n = len(matrix), len(matrix[0])
        dp = [list(map(int, matrix[0]))]
        for i in range(1, m):
            dp.append([int(matrix[i][0])])
        ans_sqrt = 1 if any(1 == x for x in dp[0]) or any(1 == dp[i][0] for i in range(1, m)) else 0
        for i in range(1, m):
            for j in range(1, n):
                for k in range(1 + dp[i - 1][j - 1]):
                    if '0' == matrix[i - k][j] or '0' == matrix[i][j - k]:
                        dp[i].append(k)
                        break
                else:
                    dp[i].append(1 + dp[i - 1][j - 1])
                ans_sqrt = max(ans_sqrt, dp[i][j])
        return ans_sqrt ** 2


sol = Solution()

example_matrix = [
    ["1", "0", "1", "0", "0"],
    ["1", "0", "1", "1", "1"],
    ["1", "1", "1", "1", "1"],
    ["1", "0", "0", "1", "0"]
]
print(sol.maximalSquare(example_matrix))
