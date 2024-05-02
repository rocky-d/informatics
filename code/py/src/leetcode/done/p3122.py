from rockyutil.leetcode import *


class Solution:
    def minimumOperations(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        cols = [Counter() for _ in range(n)]
        for i, row in enumerate(grid):
            for j, val in enumerate(row):
                cols[j][val] += 1
        dp = [0] * 10
        for col in cols:
            dp_lst, dp = sorted(enumerate(dp), key = lambda item: item[1]), []
            for val in range(10):
                dp.append(m - col[val] + dp_lst[1 if val == dp_lst[0][0] else 0][1])
        return min(dp)
