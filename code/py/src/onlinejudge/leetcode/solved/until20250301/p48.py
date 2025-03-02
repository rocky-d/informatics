from onlinejudge.leetcode import *


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        deepcopy_matrix = deepcopy(matrix)
        for i in range(n):
            for j in range(n):
                matrix[i][j] = deepcopy_matrix[-1 - j][i]
