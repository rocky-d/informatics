from heapq import heappop, heappush
from math import inf


def dijkstra(graph, start, initial = 0):
    n = len(graph)
    dsts = [inf] * n
    dsts[start] = initial
    pres = [set() for _ in range(n)]
    heap = []
    heappush(heap, (dsts[start], start))
    while 0 < len(heap):
        u_dst, u = heappop(heap)
        if u_dst != dsts[u]:  # if u_dst > dsts[u]:
            continue
        for v, w in graph[u]:
            v_dst = u_dst + w
            if v_dst < dsts[v]:
                heappush(heap, (v_dst, v))
                dsts[v] = v_dst
                pres[v].clear()
                pres[v].add(u)
            elif v_dst == dsts[v]:
                pres[v].add(u)
    return dsts, pres


def floyd(graph, initial = 0):
    n = len(graph)
    range_n = range(n)
    dp = [[inf] * i + [initial] + [inf] * (n - i - 1) for i in range_n]
    for u, vs in enumerate(graph):
        for v, w in vs:
            dp[u][v] = w
    for k in range_n:
        for u in range_n:
            for v in range_n:
                dp[u][v] = min(dp[u][v], dp[u][k] + dp[k][v])
    return dp


if __name__ == '__main__':
    print_ = lambda __iterable: print(*__iterable, sep = '\n', end = '\n\n')

    graph = [
        [],
        [(2, 2), (3, 5), (4, 4)],
        [(3, 2), (4, 1)],
        [(4, 3)],
        [],
    ]
    for start in range(len(graph)):
        print_(dijkstra(graph, start, initial = 0))
    print_(floyd(graph, initial = 0))
