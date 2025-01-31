from onlinejudge.leetcode import *


class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        range_n = range(n)
        dirs = (0, -1), (-1, 0), (0, +1), (+1, 0)
        islands, island = {}, -1
        for x, y in product(range_n, range_n):
            if 1 != grid[x][y]:
                continue
            grid[x][y] = island
            size = 1
            que = deque([(x, y)])
            while 0 < len(que):
                x, y = que.popleft()
                for dx, dy in dirs:
                    dx += x
                    dy += y
                    if not (0 <= dx < n and 0 <= dy < n) or 1 != grid[dx][dy]:
                        continue
                    grid[dx][dy] = island
                    size += 1
                    que.append((dx, dy))
            islands[island] = size
            island -= 1
        ans = max(islands.values(), default=0)
        for x, y in product(range_n, range_n):
            if 0 != grid[x][y]:
                continue
            ans = max(ans, 1 + sum(islands[island] for island in frozenset(grid[dx][dy] for dx, dy in ((dx + x, dy + y) for dx, dy in dirs) if 0 <= dx < n and 0 <= dy < n and 0 != grid[dx][dy])))
        return ans


eg_grid = [
    [1, 0, 0, 1, 1],
    [1, 0, 0, 1, 0],
    [1, 1, 1, 1, 1],
    [1, 1, 1, 0, 1],
    [0, 0, 0, 1, 0],
]
print(Solution().largestIsland(eg_grid))
