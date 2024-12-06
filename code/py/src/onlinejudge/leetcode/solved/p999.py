from onlinejudge.leetcode import *


class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        ans = 0
        m, n = len(board), len(board[0])
        for i, row in enumerate(board):
            for j, cell in enumerate(row):
                if 'R' == cell:
                    for dx, dy in (-1, 0), (0, -1), (+1, 0), (0, +1):
                        x, y = i + dx, j + dy
                        while 0 <= x < m and 0 <= y < n:
                            if 'p' == board[x][y]:
                                ans += 1
                                break
                            elif 'B' == board[x][y]:
                                break
                            x += dx
                            y += dy
                    break
        return ans


eg_board = [
    [".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", "p", ".", ".", ".", "."],
    [".", ".", ".", "R", ".", ".", ".", "p"],
    [".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", "p", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", "."],
]
print(Solution().numRookCaptures(eg_board))
