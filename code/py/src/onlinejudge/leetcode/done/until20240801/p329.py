from onlinejudge.leetcode import *


class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        def dfs(a: int, b: int, path: list[tuple[int, int]]) -> int:
            if -1 != dp[a][b]:
                return dp[a][b]
            a_1, b_1, a1, b1 = a - 1, b - 1, a + 1, b + 1
            new_path = path + [(a, b)]
            res = 1
            if -1 < a_1 and matrix[a_1][b] < matrix[a][b] and (a_1, b) not in path:
                res = max(res, 1 + dfs(a = a_1, b = b, path = new_path))
            if -1 < b_1 and matrix[a][b_1] < matrix[a][b] and (a, b_1) not in path:
                res = max(res, 1 + dfs(a = a, b = b_1, path = new_path))
            if a1 < m and matrix[a1][b] < matrix[a][b] and (a1, b) not in path:
                res = max(res, 1 + dfs(a = a1, b = b, path = new_path))
            if b1 < n and matrix[a][b1] < matrix[a][b] and (a, b1) not in path:
                res = max(res, 1 + dfs(a = a, b = b1, path = new_path))
            return res

        m, n = len(matrix), len(matrix[0])
        dp = [[-1 for _j in range(n)] for _i in range(m)]
        ans = 0
        for i in range(m):
            for j in range(n):
                dp[i][j] = dfs(a = i, b = j, path = [])
                ans = max(ans, dp[i][j])
        return ans


sol = Solution()

# 7 8 9
# 9 7 6
# 7 2 3
eg_matrix = [[7, 8, 9], [9, 7, 6], [7, 2, 3]]
print(sol.longestIncreasingPath(matrix = eg_matrix))
