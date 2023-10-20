from leetcode.leetcode import *


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [
            [True, True, True, True, True, True, True, True, True, True],
            [True, True, True, True, True, True, True, True, True, True],
            [True, True, True, True, True, True, True, True, True, True],
            [True, True, True, True, True, True, True, True, True, True],
            [True, True, True, True, True, True, True, True, True, True],
            [True, True, True, True, True, True, True, True, True, True],
            [True, True, True, True, True, True, True, True, True, True],
            [True, True, True, True, True, True, True, True, True, True],
            [True, True, True, True, True, True, True, True, True, True]
        ]
        columns = [
            [True, True, True, True, True, True, True, True, True, True],
            [True, True, True, True, True, True, True, True, True, True],
            [True, True, True, True, True, True, True, True, True, True],
            [True, True, True, True, True, True, True, True, True, True],
            [True, True, True, True, True, True, True, True, True, True],
            [True, True, True, True, True, True, True, True, True, True],
            [True, True, True, True, True, True, True, True, True, True],
            [True, True, True, True, True, True, True, True, True, True],
            [True, True, True, True, True, True, True, True, True, True]
        ]
        matrixes = [
            [True, True, True, True, True, True, True, True, True, True],
            [True, True, True, True, True, True, True, True, True, True],
            [True, True, True, True, True, True, True, True, True, True],
            [True, True, True, True, True, True, True, True, True, True],
            [True, True, True, True, True, True, True, True, True, True],
            [True, True, True, True, True, True, True, True, True, True],
            [True, True, True, True, True, True, True, True, True, True],
            [True, True, True, True, True, True, True, True, True, True],
            [True, True, True, True, True, True, True, True, True, True]
        ]
        matrix_transfer = (
            (0, 0, 0, 1, 1, 1, 2, 2, 2),
            (0, 0, 0, 1, 1, 1, 2, 2, 2),
            (0, 0, 0, 1, 1, 1, 2, 2, 2),
            (3, 3, 3, 4, 4, 4, 5, 5, 5),
            (3, 3, 3, 4, 4, 4, 5, 5, 5),
            (3, 3, 3, 4, 4, 4, 5, 5, 5),
            (6, 6, 6, 7, 7, 7, 8, 8, 8),
            (6, 6, 6, 7, 7, 7, 8, 8, 8),
            (6, 6, 6, 7, 7, 7, 8, 8, 8)
        )

        for row in range(9):
            for column in range(9):
                num = board[row][column]
                if '.' == num:
                    continue
                num = int(num)

                if rows[row][num]:
                    rows[row][num] = False
                else:
                    return False

                if columns[column][num]:
                    columns[column][num] = False
                else:
                    return False

                if matrixes[matrix_transfer[row][column]][num]:
                    matrixes[matrix_transfer[row][column]][num] = False
                else:
                    return False
        return True
