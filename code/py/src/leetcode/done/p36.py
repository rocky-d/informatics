from leetcode.util import *


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        empty_ls = [False for _ in range(9)]

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

        for i in range(3):
            for j in range(3):
                iii = 3 * i
                jjj = 3 * j
                ls = empty_ls.copy()
                for ii in range(iii, iii + 3):
                    for jj in range(jjj, jjj + 3):
                        if board[ii][jj] != '.':
                            num = int(board[ii][jj])
                            if ls[num]:
                                return False
                            else:
                                ls[num] = True
        return True
