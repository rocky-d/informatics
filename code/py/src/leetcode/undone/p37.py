from leetcode.leetcode import *


class Solution:
    matrix_transfer = (
        ((0, 0), (0, 0), (0, 0), (0, 3), (0, 3), (0, 3), (0, 6), (0, 6), (0, 6)),
        ((0, 0), (0, 0), (0, 0), (0, 3), (0, 3), (0, 3), (0, 6), (0, 6), (0, 6)),
        ((0, 0), (0, 0), (0, 0), (0, 3), (0, 3), (0, 3), (0, 6), (0, 6), (0, 6)),
        ((3, 0), (3, 0), (3, 0), (3, 3), (3, 3), (3, 3), (3, 6), (3, 6), (3, 6)),
        ((3, 0), (3, 0), (3, 0), (3, 3), (3, 3), (3, 3), (3, 6), (3, 6), (3, 6)),
        ((3, 0), (3, 0), (3, 0), (3, 3), (3, 3), (3, 3), (3, 6), (3, 6), (3, 6)),
        ((6, 0), (6, 0), (6, 0), (6, 3), (6, 3), (6, 3), (6, 6), (6, 6), (6, 6)),
        ((6, 0), (6, 0), (6, 0), (6, 3), (6, 3), (6, 3), (6, 6), (6, 6), (6, 6)),
        ((6, 0), (6, 0), (6, 0), (6, 3), (6, 3), (6, 3), (6, 6), (6, 6), (6, 6))
    )

    @staticmethod
    def update_tag_map(tag_map: List[List[List[int | bool]]], num: int, row: int, column: int):
        for i in range(9):
            # if i == row:
            #     continue
            if tag_map[i][column][num]:
                tag_map[i][column][num] = False
                tag_map[i][column][0] -= 1

        for j in range(9):
            # if j == column:
            #     continue
            if tag_map[row][j][num]:
                tag_map[row][j][num] = False
                tag_map[row][j][0] -= 1

        # i_origin = 3 * (row // 3)
        # j_origin = 3 * (column // 3)
        i_origin, j_origin = Solution.matrix_transfer[row][column]
        for i in range(i_origin, i_origin + 3):
            if i == row:
                continue
            for j in range(j_origin, j_origin + 3):
                # if j == column:
                #     continue
                if tag_map[i][j][num]:
                    tag_map[i][j][num] = False
                    tag_map[i][j][0] -= 1

    def solveSudoku(self, board: List[List[str]]) -> None:
        FILLED_TAG = [0, False, False, False, False, False, False, False, False, False]
        tag_map = [[[9] + [True for ___ in range(9)] for __ in range(9)] for _ in range(9)]

        for row in range(9):
            for column in range(9):
                num = board[row][column]
                if '.' == num:
                    continue
                num = int(num)
                tag_map[row][column] = FILLED_TAG
                Solution.update_tag_map(tag_map, num, row, column)

        stack = []
        for row in range(9):
            for column in range(9):
                if 1 == tag_map[row][column][0]:
                    stack.append((row, column))

        while stack:
            row, column = stack.pop()
            num = 1 + tag_map[row][column][1:].index(True)
            board[row][column] = str(num)
            tag_map[row][column] = FILLED_TAG
            Solution.update_tag_map(tag_map, num, row, column)
            for row in range(9):
                for column in range(9):
                    if 1 == tag_map[row][column][0] and (row, column) not in stack:
                        stack.append((row, column))

        for i in range(9):
            for j in range(9):
                tags = ''
                for k in range(1, 10):
                    if tag_map[i][j][k]:
                        tags += str(k)
                print(tags, end = ', ')
            print()


sol = Solution()

board = [[".", ".", "9", "7", "4", "8", ".", ".", "."],
         ["7", ".", ".", ".", ".", ".", ".", ".", "."],
         [".", "2", ".", "1", ".", "9", ".", ".", "."],
         [".", ".", "7", ".", ".", ".", "2", "4", "."],
         [".", "6", "4", ".", "1", ".", "5", "9", "."],
         [".", "9", "8", ".", ".", ".", "3", ".", "."],
         [".", ".", ".", "8", ".", "3", ".", "2", "."],
         [".", ".", ".", ".", ".", ".", ".", ".", "6"],
         [".", ".", ".", "2", "7", "5", "9", ".", "."]]
sol.solveSudoku(board)
print(board)
