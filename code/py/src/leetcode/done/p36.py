from leetcode.util import *


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        empty_ls = [False for _ in range(10)]

        for i in range(9):
            ls = empty_ls.copy()
            for j in range(9):
                if board[i][j] != '.':
                    num = int(board[i][j])
                    if ls[num]:
                        return False
                    else:
                        ls[num] = True

        for j in range(9):
            ls = empty_ls.copy()
            for i in range(9):
                if board[i][j] != '.':
                    num = int(board[i][j])
                    if ls[num]:
                        return False
                    else:
                        ls[num] = True

        for i_origin in range(0, 7, 3):
            for j_origin in range(0, 7, 3):
                ls = empty_ls.copy()
                for i in range(i_origin, i_origin + 3):
                    for j in range(j_origin, j_origin + 3):
                        if board[i][j] != '.':
                            num = int(board[i][j])
                            if ls[num]:
                                return False
                            else:
                                ls[num] = True
        return True
