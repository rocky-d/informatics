from rockyutil.leetcode import *


class Solution:
    def findAnswer(self, n: int, edges: List[List[int]]) -> List[bool]:
        ans = [False] * len(edges)
        graph = [[] for _ in range(n)]
        edges_idxes = {}
        for i, (a, b, w) in enumerate(edges):
            graph[a].append((b, w))
            graph[b].append((a, w))
            edges_idxes[a, b] = i
            edges_idxes[b, a] = i
        dsts = [inf] * n
        dsts[0] = 0
        pres = [[] for _ in range(n)]
        heap = []
        heappush(heap, (dsts[0], 0))
        while 0 < len(heap):
            dst, node = heappop(heap)
            if dst != dsts[node]:
                continue
            for nxt, cost in graph[node]:
                if dst + cost == dsts[nxt]:
                    pres[nxt].append(node)
                elif dst + cost < dsts[nxt]:
                    pres[nxt].clear()
                    pres[nxt].append(node)
                    dsts[nxt] = dst + cost
                    heappush(heap, (dsts[nxt], nxt))
        que = deque([n - 1])
        while 0 < len(que):
            node = que.popleft()
            for nxt in pres[node]:
                que.append(nxt)
                if (node, nxt) in edges_idxes.keys():
                    ans[edges_idxes[node, nxt]] = True
        return ans
