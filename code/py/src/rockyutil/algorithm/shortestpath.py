from heapq import heappop, heappush
from math import inf


def dijkstra(graph, start):
    n = len(graph)
    dsts = [inf] * n
    dsts[start] = 0
    pres = [None] * n
    seen = [False] * n
    heap = []
    heappush(heap, (dsts[start], start))
    while 0 < len(heap):
        dst, node = heappop(heap)
        while 0 < len(heap) and seen[node]:
            dst, node = heappop(heap)
        seen[node] = True
        for nxt, cost in graph[node]:
            if dst + cost < dsts[nxt]:
                dsts[nxt] = dst + cost
                pres[nxt] = node
                heappush(heap, (dsts[nxt], nxt))


if __name__ == '__main__':
    dijkstra(
        [
            [],
            [(2, 2), (3, 5), (4, 4)],
            [(3, 2), (4, 1)],
            [(4, 3)],
            [],
        ],
        1,
    )
