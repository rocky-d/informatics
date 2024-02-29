from rockyutil.leetcode import *


class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = [[] for _ in range(n)]
        for fr, to, price in flights:
            graph[fr].append((to, price))
        dists = [inf for _ in range(n)]
        dists[src] = 0
        seen = {src}
        heap_min = [(0, -1, src)]
        for _ in range(n):
            spend, trans, fr = heappop(heap_min)
            while spend != dists[fr]:
                spend, trans, fr = heappushpop(heap_min, (dists[fr], trans, fr))
            if k < trans + 1:
                continue
            for to, price in graph[fr]:
                if spend + price < dists[to]:
                    dists[to] = spend + price
                    if to not in seen:
                        seen.add(to)
                        heappush(heap_min, (dists[to], trans + 1, to))
        return -1 if isinf(dists[dst]) else dists[dst]


eg_n = 3
eg_flights = [
    [0, 1, 100],
    [1, 2, 100],
    [0, 2, 500],
]
eg_src = 0
eg_dst = 2
eg_k = 1
print(Solution().findCheapestPrice(eg_n, eg_flights, eg_src, eg_dst, eg_k))
