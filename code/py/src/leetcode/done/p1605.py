from rockyutil.leetcode import *


class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        ans = [[0] * len(colSum) for _ in range(len(rowSum))]
        rows, cols = [0] * len(rowSum), [0] * len(colSum)
        for i, x in enumerate(rowSum):
            for j, y in enumerate(colSum):
                num = min(x - rows[i], y - cols[j])
                rows[i] += num
                cols[j] += num
                ans[i][j] = num
        return ans
