from rockyutil.leetcode import *


class Solution:
    def minimumOperations(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        cols = [Counter() for _ in range(n)]
        for i, row in enumerate(grid):
            for j, val in enumerate(row):
                cols[j][val] += 1
        dp = [m - cols[0][val] for val in range(10)]
        for col in range(1, n):
            col = cols[col]
            dp_lst, dp = dp, []
            dp_idxes = sorted(enumerate(dp_lst), key = lambda item: item[1])
            for val in range(10):
                if dp_idxes[0][0] != val:
                    dp.append(dp_idxes[0][1] + m - col[val])
                else:
                    dp.append(dp_idxes[1][1] + m - col[val])
        return min(dp)
