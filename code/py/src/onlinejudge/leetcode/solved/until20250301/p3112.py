from onlinejudge.leetcode import *


class Solution:
    def minimumTime(self, n: int, edges: List[List[int]], disappear: List[int]) -> List[int]:
        graph = [[] for _ in range(n)]
        for u, v, w in edges:
            graph[u].append((v, w))
            graph[v].append((u, w))
        dsts = [inf] * n
        dsts[0] = 0
        heap = []
        heappush(heap, (dsts[0], 0))
        while 0 < len(heap):
            u_dst, u = heappop(heap)
            if u_dst != dsts[u]:
                continue
            for v, w in graph[u]:
                v_dst = u_dst + w
                if v_dst < dsts[v] and v_dst < disappear[v]:
                    dsts[v] = v_dst
                    heappush(heap, (v_dst, v))
        return [-1 if isinf(dst) else dst for dst in dsts]
