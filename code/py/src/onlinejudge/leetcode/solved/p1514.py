from onlinejudge.leetcode import *


class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        graph = [[] for _ in range(n)]
        for (u, v), w in zip(edges, succProb):
            graph[u].append((v, w))
            graph[v].append((u, w))
        dsts = [-0.0] * n
        dsts[start_node] = -1
        heap = []
        heappush(heap, (dsts[start_node], start_node))
        while 0 < len(heap):
            u_dst, u = heappop(heap)
            if u_dst != dsts[u]:
                continue
            for v, w in graph[u]:
                v_dst = u_dst * w
                if v_dst < dsts[v]:
                    heappush(heap, (v_dst, v))
                    dsts[v] = v_dst
        return -dsts[end_node]
