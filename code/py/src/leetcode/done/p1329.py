from rockyutil.leetcode import *


class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        ans = [[...] * n for _ in range(m)]
        for i in range(m - 1, 0, -1):
            nums = []
            for j in range(min(n, m - i)):
                nums.append(mat[i + j][j])
            for j, val in enumerate(sorted(nums)):
                ans[i + j][j] = val
        for i in range(n - 1, 0, -1):
            nums = []
            for j in range(min(m, n - i)):
                nums.append(mat[j][i + j])
            for j, val in enumerate(sorted(nums)):
                ans[j][i + j] = val
        nums = []
        for i in range(min(m, n)):
            nums.append(mat[i][i])
        for i, val in enumerate(sorted(nums)):
            ans[i][i] = val
        return ans
