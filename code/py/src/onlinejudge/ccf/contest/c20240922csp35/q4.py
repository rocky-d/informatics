from heapq import heappop, heappush
from itertools import combinations
from math import inf, isinf


def main():
    n, m = map(int, input().split())
    cords = (map(int, input().split()) for _ in range(n))
    stations = (map(int, input().split()) for _ in range(m))

    graph = [{} for _ in range(n)]
    cords = list(map(tuple, cords))
    for x, y, r, t in stations:
        ls = []
        for i, cord in enumerate(cords):
            if abs(x - cord[0]) <= r and abs(y - cord[1]) <= r:
                ls.append(i)
        for u, v in combinations(ls, r=2):
            if v not in graph[u] or t < graph[u][v]:
                graph[u][v] = t
            if u not in graph[v] or t < graph[v][u]:
                graph[v][u] = t

    dsts  = [inf] * n
    dsts[0] = 0
    heap = []
    heappush(heap, (dsts[0], 0))
    while heap:
        u_dst, u = heappop(heap)
        if u_dst != dsts[u]:
            continue
        for v, w in graph[u].items():
            v_dst = u_dst + w
            if v_dst < dsts[v]:
                dsts[v] = v_dst
                heappush(heap, (v_dst, v))
    print('Nan' if isinf(dsts[-1]) else dsts[-1])


if __name__ == '__main__':
    main()
