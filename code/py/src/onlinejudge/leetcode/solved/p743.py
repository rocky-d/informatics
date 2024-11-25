from onlinejudge.leetcode import *


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = [None] + [[] for _ in range(n)]
        for u, v, w in times:
            graph[u].append((v, w))
        dsts = [-1] + [inf] * n
        dsts[k] = 0
        heap = []
        heappush(heap, (dsts[k], k))
        while 0 < len(heap):
            u_dst, u = heappop(heap)
            if u_dst != dsts[u]:  # if u_dst > dsts[u]:
                continue
            for v, w in graph[u]:
                v_dst = u_dst + w
                if v_dst < dsts[v]:
                    dsts[v] = v_dst
                    heappush(heap, (v_dst, v))
        maxm = max(dsts)
        return -1 if isinf(maxm) else maxm
