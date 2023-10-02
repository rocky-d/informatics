from leetcode.util import *


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        num_dict = {'1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
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
                if board[row][column] == '.':
                    continue
                num = num_dict[board[row][column]]

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
