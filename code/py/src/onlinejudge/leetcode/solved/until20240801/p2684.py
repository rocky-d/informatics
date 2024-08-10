from onlinejudge.leetcode import *


class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [True for _ in grid]
        for col in range(1, n):
            dp_lst, dp = dp, [False for _ in grid]
            not_moved = True
            for row in range(m):
                focus = grid[row][col]
                for row_lst in map(lambda ofst: row + ofst, (-1, 0, 1)):
                    if row_lst < 0 or m <= row_lst:
                        continue
                    if dp_lst[row_lst] and grid[row_lst][col - 1] < focus:
                        dp[row] = True
                        not_moved = False
            if not_moved:
                ans = col - 1
                break
        else:
            ans = n - 1
        return ans
