from onlinejudge.leetcode import *


class neighborSum:
    def __init__(self, grid: List[List[int]]) -> None:
        self.m = len(grid)
        self.n = len(grid[0])
        self.grid = grid
        self.map = {}
        for i in range(self.m):
            for j in range(self.n):
                self.map[grid[i][j]] = i, j

    def adjacentSum(self, value: int) -> int:
        res = 0
        dirs = (0, -1), (0, +1), (-1, 0), (+1, 0)
        x, y = self.map[value]
        for dx, dy in dirs:
            dx += x
            dy += y
            if 0 <= dx < self.m and 0 <= dy < self.n:
                res += self.grid[dx][dy]
        return res

    def diagonalSum(self, value: int) -> int:
        res = 0
        dirs = (-1, -1), (-1, +1), (+1, -1), (+1, +1)
        x, y = self.map[value]
        for dx, dy in dirs:
            dx += x
            dy += y
            if 0 <= dx < self.m and 0 <= dy < self.n:
                res += self.grid[dx][dy]
        return res
