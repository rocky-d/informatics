from rockyutil.leetcode import *


class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        m, n = len(matrix), len(matrix[0])
        ans = 0
        pre = [[0 for _ in range(1 + n)] for _ in range(1 + m)]
        for i in range(m):
            for j in range(n):
                pre[i + 1][j + 1] = matrix[i][j] + pre[i + 1][j] + pre[i][j + 1] - pre[i][j]
        for i in range(m):
            for j in range(n):
                for i_ in range(i + 1):
                    for j_ in range(j + 1):
                        if target == pre[i + 1][j + 1] - pre[i + 1][j_] - pre[i_][j + 1] + pre[i_][j_]:
                            ans += 1
        return ans


eg_matrix = [
    [0, 1, 0],
    [1, 1, 1],
    [0, 1, 0],
]
eg_target = 0
print(Solution().numSubmatrixSumTarget(matrix = eg_matrix, target = eg_target))
