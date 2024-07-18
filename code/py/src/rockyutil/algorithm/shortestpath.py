from heapq import heappop, heappush
from math import inf


def dijkstra(graph, start):
    n = len(graph)
    dsts = [inf] * n
    dsts[start] = 0
    pres = [None] * n
    heap = []
    heappush(heap, (dsts[start], start))
    while 0 < len(heap):
        u_dst, u = heappop(heap)
        if u_dst != dsts[u]:  # if u_dst > dsts[u]:
            continue
        for v, w in graph[u]:
            v_dst = u_dst + w
            if v_dst < dsts[v]:
                dsts[v], pres[v] = v_dst, u
                heappush(heap, (v_dst, v))


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
