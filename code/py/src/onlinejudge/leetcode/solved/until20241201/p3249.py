from onlinejudge.leetcode import *


class Solution:
    def countGoodNodes(self, edges: List[List[int]]) -> int:
        n = len(edges) + 1
        graph = [[] for _ in range(n)]
        ins = [0] * n
        ins[0] += 1
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
            ins[u] += 1
            ins[v] += 1
        cnter = [[] for _ in range(n)]
        vis = [False] * n
        que = deque(x for x, cnt in enumerate(ins) if 1 == cnt)
        for x in que:
            vis[x] = True
        while 0 < len(que):
            u = que.popleft()
            for v in graph[u]:
                if vis[v]:
                    continue
                cnter[v].append(1 + sum(cnter[u]))
                ins[v] -= 1
                if 1 == ins[v]:
                    que.append(v)
                    vis[v] = True
        return sum(1 for ls in cnter if 0 == len(ls) or all(ls[0] == x for x in ls))
