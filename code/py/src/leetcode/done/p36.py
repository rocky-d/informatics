from leetcode.util import *


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        num_dict = {'.': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}

        for i in range(9):
            ls = [True, True, True, True, True, True, True, True, True, True]
            for j in range(9):
                num = num_dict[board[i][j]]
                if num == 0 or ls[num]:
                    ls[num] = False
                else:
                    return False

        for j in range(9):
            ls = [True, True, True, True, True, True, True, True, True, True]
            for i in range(9):
                num = num_dict[board[i][j]]
                if num == 0 or ls[num]:
                    ls[num] = False
                else:
                    return False

        for i_origin, j_origin in ((0, 0), (0, 3), (0, 6), (3, 0), (3, 3), (3, 6), (6, 0), (6, 3), (6, 6)):
            ls = [True, True, True, True, True, True, True, True, True, True]
            for i in range(i_origin, i_origin + 3):
                for j in range(j_origin, j_origin + 3):
                    num = num_dict[board[i][j]]
                    if num == 0 or ls[num]:
                        ls[num] = False
                    else:
                        return False
        return True
