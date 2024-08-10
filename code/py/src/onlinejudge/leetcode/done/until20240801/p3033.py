from onlinejudge.leetcode import *


class Solution:
    def modifiedMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        m, n = len(matrix), len(matrix[0])
        col_max = {}
        for row in matrix:
            for j in range(n):
                if -1 == row[j]:
                    if j not in col_max.keys():
                        col_max[j] = max(matrix[i][j] for i in range(m))
                    row[j] = col_max[j]
        return matrix
