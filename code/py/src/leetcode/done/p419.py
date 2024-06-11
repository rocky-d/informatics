from rockyutil.leetcode import *


class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        return sum(1 for i, row in enumerate(board) for j, val in enumerate(row) if 'X' == val and (0 == i or 'X' != board[i - 1][j]) and (0 == j or 'X' != row[j - 1]))
