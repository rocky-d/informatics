from rockyutil.leetcode import *


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m, n = len(matrix), len(matrix[0])
        rows, cols = set(), set()
        for row, matrix_row in enumerate(matrix):
            for col, matrix_val in enumerate(matrix_row):
                if 0 == matrix_val:
                    rows.add(row), cols.add(col)
        for row, matrix_row in enumerate(matrix):
            if row in rows:
                for col in range(n):
                    matrix_row[col] = 0
            else:  # elif row not in rows:
                for col in range(n):
                    if col in cols:
                        matrix_row[col] = 0
