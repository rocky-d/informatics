from rockyutil.leetcode import *


class Graph:
    def __init__(self, n: int, edges: List[List[int]]) -> None:
        self.graph = [deque() for _ in range(n)]
        for fr, to, cost in edges:
            self.graph[fr].append((to, cost))

    def addEdge(self, edge: List[int]) -> None:
        fr, to, cost = edge
        self.graph[fr].append((to, cost))

    def shortestPath(self, node1: int, node2: int) -> int:
        seen = set()
        dsts, heap = [inf for _ in self.graph], []
        dsts[node1] = 0
        heappush(heap, (dsts[node1], node1))
        while 0 < len(heap):
            dst, node = heappop(heap)
            while node in seen and 0 < len(heap):
                dst, node = heappop(heap)
            seen.add(node)
            if node == node2:
                res = dst
                break
            for nxt, cost in self.graph[node]:
                if dst + cost < dsts[nxt]:
                    dsts[nxt] = dst + cost
                    heappush(heap, (dsts[nxt], nxt))
        else:
            res = -1
        return res
