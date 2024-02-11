from rockyutil.leetcode import *


class Solution:
    def modifiedMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        m, n = len(matrix), len(matrix[0])
        col_max = [0 for _ in range(n)]
        for row in range(m):
            for col in range(n):
                col_max[col] = max(col_max[col], matrix[row][col])
        for row in range(m):
            for col in range(n):
                if matrix[row][col] == -1:
                    matrix[row][col] = col_max[col]
        return matrix
