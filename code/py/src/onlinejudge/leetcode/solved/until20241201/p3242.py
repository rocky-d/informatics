from onlinejudge.leetcode import *


class NeighborSum:
    def __init__(self, grid: List[List[int]]) -> None:
        n = len(grid)
        nn = n * n
        adjs = [...] * nn
        dias = [...] * nn
        for x, row in enumerate(grid):
            for y, val in enumerate(row):
                adj = 0
                for dx, dy in (0, -1), (-1, 0), (0, +1), (+1, 0):
                    dx += x
                    dy += y
                    if 0 <= dx < n and 0 <= dy < n:
                        adj += grid[dx][dy]
                adjs[val] = adj
                dia = 0
                for dx, dy in (-1, -1), (+1, -1), (-1, +1), (+1, +1):
                    dx += x
                    dy += y
                    if 0 <= dx < n and 0 <= dy < n:
                        dia += grid[dx][dy]
                dias[val] = dia
        self.adjs = adjs
        self.dias = dias

    def adjacentSum(self, value: int) -> int:
        return self.adjs[value]

    def diagonalSum(self, value: int) -> int:
        return self.dias[value]
