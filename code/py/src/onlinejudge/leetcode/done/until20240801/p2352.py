from onlinejudge.leetcode import *


class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        n = len(grid)
        rows_cnter = Counter(map(tuple, grid))
        return sum(rows_cnter[tuple(grid[row][col] for row in range(n))] for col in range(n))


eg_grid = [
    [3, 1, 2, 2],
    [1, 4, 4, 5],
    [2, 4, 2, 2],
    [2, 4, 2, 2],
]
print(Solution().equalPairs(eg_grid))
