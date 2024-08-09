from rockyutil.leetcode import *


class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        return sum(
            1 for i, j in product(range(len(grid) - 2), range(len(grid[0]) - 2)) if 15 ==
            sum(grid[i + 0][j:j + 3]) ==
            sum(grid[i + 1][j:j + 3]) ==
            sum(grid[i + 2][j:j + 3]) ==
            grid[i + 0][j + 0] + grid[i + 1][j + 0] + grid[i + 2][j + 0] ==
            grid[i + 0][j + 1] + grid[i + 1][j + 1] + grid[i + 2][j + 1] ==
            grid[i + 0][j + 2] + grid[i + 1][j + 2] + grid[i + 2][j + 2] ==
            grid[i + 0][j + 0] + grid[i + 1][j + 1] + grid[i + 2][j + 2] ==
            grid[i + 0][j + 2] + grid[i + 1][j + 1] + grid[i + 2][j + 0] and
            [1, 2, 3, 4, 5, 6, 7, 8, 9] ==
            sorted(chain(grid[i + 0][j:j + 3], grid[i + 1][j:j + 3], grid[i + 2][j:j + 3]))
        )


eg_grid = [
    [5, 5, 5],
    [5, 5, 5],
    [5, 5, 5],
]
print(Solution().numMagicSquaresInside(eg_grid))
