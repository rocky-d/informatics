from onlinejudge.leetcode import *


class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        grid = reduce(add, grid)
        mn = len(grid)
        dsts = [inf] * mn
        dsts[0] = 0
        heap = []
        heappush(heap, (dsts[0], 0))
        while 0 < len(heap):
            u_dst, u = heappop(heap)
            if u_dst != dsts[u]:
                continue
            for i, v in enumerate((u + 1, u - 1, u + n, u - n), start=1):
                if v == u + 1 and 0 == (u + 1) % n:
                    continue
                elif v == u - 1 and 0 == u % n:
                    continue
                elif v == u + n and mn - n <= u:
                    continue
                elif v == u - n and u < n:
                    continue
                v_dst = u_dst if i == grid[u] else u_dst + 1
                if v_dst < dsts[v]:
                    dsts[v] = v_dst
                    heappush(heap, (v_dst, v))
        return dsts[-1]


eg_grid = [
    [1, 1, 1, 1],
    [2, 2, 2, 2],
    [1, 1, 1, 1],
    [2, 2, 2, 2],
]
print(Solution().minCost(eg_grid))
