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
        dsts = [inf for _ in range(n)]
        dsts[0] = 0
        ancestors = [[] for _ in range(n)]
        seen = set()
        heap = []
        heappush(heap, (0, 0))
        while 0 < len(heap):
            dst, node = heappop(heap)
            while node in seen and 0 < len(heap):
                dst, node = heappop(heap)
            seen.add(node)
            if node == n - 1:
                break
            for nxt, cost in graph[node]:
                if dst + cost == dsts[nxt]:
                    ancestors[nxt].append(node)
                elif dst + cost < dsts[nxt]:
                    ancestors[nxt].clear()
                    ancestors[nxt].append(node)
                    dsts[nxt] = dst + cost
                    heappush(heap, (dsts[nxt], nxt))
        que = deque([n - 1])
        while 0 < len(que):
            node = que.popleft()
            for nxt in ancestors[node]:
                que.append(nxt)
                if (node, nxt) in edges_idxes:
                    ans[edges_idxes[node, nxt]] = True
                elif (nxt, node) in edges_idxes:
                    ans[edges_idxes[nxt, node]] = True
        return ans


eg_n = 6
eg_edges = [[0, 1, 4], [0, 2, 1], [1, 3, 2], [1, 4, 3], [1, 5, 1], [2, 3, 1], [3, 5, 3], [4, 5, 2]]
print(Solution().findAnswer(eg_n, eg_edges))
