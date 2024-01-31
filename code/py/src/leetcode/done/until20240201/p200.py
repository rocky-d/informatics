from rockyutil.datastructure.unionfind import UnionFindDict
from rockyutil.leetcode import *


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        ufd = UnionFindDict((), grouped = True)
        for i in range(m):
            for j in range(n):
                if '1' == grid[i][j]:
                    ufd._heads[i, j] = i, j
                    ufd._groups[i, j] = i, j
                    if 0 <= i - 1 and '1' == grid[i - 1][j]:
                        ufd.union(a = (i, j), b = (i - 1, j))
                    if 0 <= j - 1 and '1' == grid[i][j - 1]:
                        ufd.union(a = (i, j), b = (i, j - 1))
        return len(ufd._groups)


eg_grid = [
    ['1', '1', '1', '1', '0'],
    ['1', '1', '0', '1', '0'],
    ['1', '1', '0', '0', '0'],
    ['0', '0', '0', '0', '0']
]
print(Solution().numIslands(grid = eg_grid))
