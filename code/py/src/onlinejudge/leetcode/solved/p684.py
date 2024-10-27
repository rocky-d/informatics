from onlinejudge.leetcode import *


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        ins = [None] + [0] * len(edges)
        graph = [None] + [[] for _ in range(len(edges))]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
            ins[u] += 1
            ins[v] += 1
        vis = set()
        dque = deque(x for x, cnt in enumerate(ins) if 1 == cnt)
        while 0 < len(dque):
            u = dque.popleft()
            vis.add(u)
            for v in graph[u]:
                ins[v] -= 1
                if 1 == ins[v]:
                    dque.append(v)
        for u, v in reversed(edges):
            if u not in vis and v not in vis:
                ans = [u, v]
                break
        return ans
