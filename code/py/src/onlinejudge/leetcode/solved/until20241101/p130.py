from onlinejudge.leetcode import *


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        m, n = len(board), len(board[0])
        seen = set()

        def dfs(x: int, y: int) -> None:
            if 'X' == board[x][y] or (x, y) in seen:
                return
            seen.add((x, y))
            for oft_a, oft_b in (0, 1), (1, 0), (0, -1), (-1, 0):
                a, b = x + oft_a, y + oft_b
                if 0 <= a < m and 0 <= b < n:
                    dfs(a, b)

        for x in range(m):
            dfs(x = x, y = 0)
            dfs(x = x, y = n - 1)
        for y in range(n):
            dfs(x = 0, y = y)
            dfs(x = m - 1, y = y)
        for x, row in enumerate(board):
            for y, val in enumerate(row):
                if 'X' != val and (x, y) not in seen:
                    row[y] = 'X'
