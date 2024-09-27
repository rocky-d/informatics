from heapq import heappop, heappush
from math import inf, isinf


def main():
    n, m = map(int, input().split())
    cords = (map(int, input().split()) for _ in range(n))
    stations = (map(int, input().split()) for _ in range(m))

    a, b = [[] for _ in range(n)], [[] for _ in range(m)]
    cords = list(map(tuple, cords))
    delays = [0] * m
    for mi, (x, y, r, t) in enumerate(stations):
        delays[mi] = t
        for ni, cord in enumerate(cords):
            if abs(x - cord[0]) <= r and abs(y - cord[1]) <= r:
                a[ni].append(mi)
                b[mi].append(ni)
    dsts  = [inf] * n
    dsts[0] = 0
    heap = []
    vis = [False] * n
    heappush(heap, (dsts[0], 0))
    final = n - 1
    while heap:
        u_dst, u = heappop(heap)
        if u_dst != dsts[u]:
            continue
        if u == final:
            break
        vis[u] = True
        for mi in a[u]:
            w = delays[mi]
            for v in b[mi]:
                if u == v or vis[v]:
                    continue
                v_dst = u_dst + w
                if v_dst < dsts[v]:
                    dsts[v] = v_dst
                    heappush(heap, (v_dst, v))
    print('Nan' if isinf(dsts[-1]) else dsts[-1])


if __name__ == '__main__':
    main()
