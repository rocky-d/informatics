from rockyutil.leetcode import *


class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        ans = [[0] * len(colSum) for _ in range(len(rowSum))]
        rows, cols = [0] * len(rowSum), [0] * len(colSum)
        for i, row in enumerate(rowSum):
            for j, col in enumerate(colSum):
                ans[i][j] = num = min(row - rows[i], col - cols[j])
                rows[i] += num
                cols[j] += num
        return ans
