from rockyutil.leetcode import *


class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        m, n = len(mat), len(mat[0])
        for i in range(m):
            mat[i] = [-1] + mat[i] + [-1]
        mat = [[-1 for _ in range(2 + n)]] + mat + [[-1 for _ in range(2 + n)]]
        for i in range(1, 1 + m):
            for j in range(1, 1 + n):
                if mat[i][j - 1] < mat[i][j] and mat[i][j] > mat[i][j + 1] and mat[i - 1][j] < mat[i][j] and mat[i][j] > mat[i + 1][j]:
                    return [i - 1, j - 1]


eg_mat = [
    [10, 20, 15],
    [21, 30, 14],
    [7, 16, 32]
]
print(Solution().findPeakGrid(mat = eg_mat))
