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
        subs = [[] for _ in range(n)]
        que = deque(x for x, cnt in enumerate(ins) if 1 == cnt)
        seen = [False] * n
        for x in que:
            seen[x] = True
        while 0 < len(que):
            u = que.popleft()
            for v in graph[u]:
                if seen[v]:
                    continue
                subs[v].append(1 + sum(subs[u]))
                ins[v] -= 1
                if 1 == ins[v]:
                    seen[v] = True
                    que.append(v)
        return sum(1 for ls in subs if 0 == len(ls) or all(ls[0] == x for x in ls))


eg_edges = [[0, 1], [1, 2], [2, 3], [3, 4], [0, 5], [1, 6], [2, 7], [3, 8]]
print(Solution().countGoodNodes(eg_edges))
