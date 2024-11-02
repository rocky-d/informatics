from onlinejudge.leetcode import *


class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        graph = [[] for _ in range(n)]
        for u, v, t in roads:
            graph[u].append((v, t))
            graph[v].append((u, t))
        dists, ways = [inf for _ in range(n)], [0 for _ in range(n)]
        dists[0], ways[0] = 0, 1
        heap_min = [(0, 0)]
        for _ in range(n):
            dst, u = heappop(heap_min)
            while dst != dists[u]:
                dst, u = heappop(heap_min)
            for v, t in graph[u]:
                t_new = dists[u] + t
                if t_new < dists[v]:
                    dists[v], ways[v] = t_new, ways[u]
                    heappush(heap_min, (dists[v], v))
                elif t_new == dists[v]:
                    ways[v] += ways[u]
        return ways[-1] % 1_000_000_007


eg_n = 6
eg_roads = [[3, 0, 4], [0, 2, 3], [1, 2, 2], [4, 1, 3], [2, 5, 5], [2, 3, 1], [0, 4, 1], [2, 4, 6], [4, 3, 1]]
print(Solution().countPaths(eg_n, eg_roads))
