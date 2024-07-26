from heapq import heappop, heappush
from math import inf


def dijkstra(graph, start, start_dst = 0):
    n = len(graph)
    dsts = [inf] * n
    dsts[start] = start_dst
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
    return dsts, pres


def floyd(graph):
    n = len(graph)
    dp = [[inf] * n for _ in range(n)]
    for u, vs in enumerate(graph):
        for v, w in vs:
            dp[u][v] = w
    for k in range(n):
        for u in range(n):
            for v in range(n):
                dp[u][v] = min(dp[u][v], dp[u][k] + dp[k][v])
    return dp


if __name__ == '__main__':
    print(*dijkstra(
        graph = [
            [],
            [(2, 2), (3, 5), (4, 4)],
            [(3, 2), (4, 1)],
            [(4, 3)],
            [],
        ],
        start = 1,
        start_dst = 0,
    ), sep = '\n')
