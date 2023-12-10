from rockyutil.leetcode import *


class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        m, n = len(matrix), len(matrix[0])
        return [[matrix[_j][_i] for _j in range(m)] for _i in range(n)]
