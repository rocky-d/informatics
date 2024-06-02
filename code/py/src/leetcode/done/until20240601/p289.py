from rockyutil.leetcode import *


class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        m, n = len(board), len(board[0])
        row = []
        for i, board_row in enumerate(board):
            row_lst, row = row, board_row.copy()
            for j, board_cell in enumerate(board_row):
                cnt = 0
                y = j - 1
                if 0 <= y < n and 1 == row[y]:
                    cnt += 1
                y = j + 1
                if 0 <= y < n and 1 == row[y]:
                    cnt += 1
                if 0 <= i - 1:
                    for y in map(lambda oft: j + oft, (-1, 0, 1)):
                        if 0 <= y < n and 1 == row_lst[y]:
                            cnt += 1
                if i + 1 < m:
                    x = i + 1
                    for y in map(lambda oft: j + oft, (-1, 0, 1)):
                        if 0 <= y < n and 1 == board[x][y]:
                            cnt += 1
                if 1 == board_cell:
                    if cnt < 2 or 3 < cnt:
                        board_row[j] = 0
                else:  # elif 0 == board_row:
                    if 3 == cnt:
                        board_row[j] = 1
