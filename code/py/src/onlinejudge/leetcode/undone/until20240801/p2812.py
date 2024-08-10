from onlinejudge.leetcode import *


class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        n = len(grid)
        q = []
        dis = [[-1] * n for _ in range(n)]
        for i, row in enumerate(grid):
            for j, x in enumerate(row):
                if x:
                    q.append((i, j))
                    dis[i][j] = 0
        groups = [q]
        while q:
            tmp = q
            q = []
            for i, j in tmp:
                for x, y in (i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1):
                    if 0 <= x < n and 0 <= y < n and dis[x][y] < 0:
                        q.append((x, y))
                        dis[x][y] = len(groups)
            groups.append(q)
        fa = list(range(n * n))

        def find(x: int) -> int:
            if fa[x] != x:
                fa[x] = find(fa[x])
            return fa[x]

        for d in range(len(groups) - 2, 0, -1):
            for i, j in groups[d]:
                for x, y in (i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1):
                    if 0 <= x < n and 0 <= y < n and dis[x][y] >= dis[i][j]:
                        fa[find(x * n + y)] = find(i * n + j)
            if find(0) == find(n * n - 1):
                return d
        return 0
