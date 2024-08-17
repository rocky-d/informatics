from onlinejudge.leetcode import *


class Solution:
    def maximumValueSum(self, board: List[List[int]]) -> int:
        ans = -3_000_000_000
        m, n = len(board), len(board[0])
        range_n = range(n)
        dp1 = [list(board[0])] + [[0] * n for _ in range(1, m - 1)]
        for i in range(1, m - 1):
            row = board[i]
            for j, val in enumerate(row):
                dp1[i][j] = max(dp1[i - 1][j], val)
        dp2 = [[0] * n for _ in range_n]
        for x, y in combinations(range_n, r = 2):
            dp2[x][y] = max(dp1[0][x] + board[1][y], dp1[0][y] + board[1][x])
        for i in range(2, m - 1):
            row = board[i]
            for x, y, z in combinations(range_n, r = 3):
                ans = max(ans, dp2[x][y] + row[z], dp2[x][z] + row[y], dp2[y][z] + row[x])
            for x, y in combinations(range_n, r = 2):
                dp2[x][y] = max(dp2[x][y], dp1[i - 1][x] + board[i][y], dp1[i - 1][y] + board[i][x])
        row = board[-1]
        for x, y, z in combinations(range_n, r = 3):
            ans = max(ans, dp2[x][y] + row[z], dp2[x][z] + row[y], dp2[y][z] + row[x])
        return ans
