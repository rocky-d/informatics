from rockyutil.leetcode import *


class Solution:
    def modifiedMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        m, n = len(matrix), len(matrix[0])
        col_max = {}
        for row in range(m):
            for col in range(n):
                if -1 == matrix[row][col]:
                    if col not in col_max:
                        col_max[col] = max(matrix[row_][col] for row_ in range(m))
                    matrix[row][col] = col_max[col]
        return matrix
