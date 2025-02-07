from onlinejudge.leetcode import *


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        ans = [[None] * n for _ in range(n)]
        x, y = 0, 0
        dirs = cycle(((0, +1), (+1, 0), (0, -1), (-1, 0)))
        dx, dy = next(dirs)
        for i in range(1, 1 + n * n):
            ans[x][y] = i
            nx = x + dx
            ny = y + dy
            if not (0 <= nx < n and 0 <= ny < n) or ans[nx][ny] is not None:
                dx, dy = next(dirs)
            x += dx
            y += dy
        return ans
