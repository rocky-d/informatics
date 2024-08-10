from onlinejudge.leetcode import *


class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = [deque() for _ in range(n)]
        for fr, to, price in flights:
            graph[fr].append((to, price))
        seen = set()
        costs, heap = [inf for _ in range(n)], []
        costs[src] = 0
        heappush(heap, (costs[src], src, 1))
        while 0 < len(heap):
            cost, node, cnt = heappop(heap)
            while (node in seen or k + 2 < cnt) and 0 < len(heap):
                cost, node, cnt = heappop(heap)
            seen.add(node)
            if node == dst:
                ans = cost
                break
            for nxt, price in graph[node]:
                if cost + price < costs[nxt]:
                    costs[nxt] = cost + price
                    heappush(heap, (costs[nxt], nxt, cnt + 1))
        else:
            ans = -1
        return ans


eg_n = 4
eg_flights = [
    [0, 1, 1],
    [0, 2, 5],
    [1, 2, 1],
    [2, 3, 1],
]
eg_src = 0
eg_dst = 3
eg_k = 1
print(Solution().findCheapestPrice(eg_n, eg_flights, eg_src, eg_dst, eg_k))
