from heapq import *
from math import inf, isinf


def main() -> None:
    n, m, s, t = map(int, input().split())
    hot = map(int, input().split())
    uvw = (map(int, input().split()) for _ in range(m))

    hot = [None] + list(hot)
    hot[s] = hot[t] = 0
    graph = [None] + [[] for _ in range(n)]
    for u, v, w in uvw:
        graph[u].append((v, w))
        graph[v].append((u, w))
    dsts = [None] + [inf] * n
    dsts[s] = 0
    pres = [None] + [[] for _ in range(n)]
    pres[s].append(hot[s])
    heap = []
    heappush(heap, (dsts[s], s))
    while 0 < len(heap):
        dst, u = heappop(heap)
        if dst != dsts[u]:
            continue
        for v, w in graph[u]:
            new_dst = dst + w
            if new_dst < dsts[v]:
                heappush(heap, (new_dst, v))
                dsts[v] = new_dst
                pres[v] = [max(hot[v], min(pres[u], default = 0))]
            elif new_dst == dsts[v]:
                pres[v].append(max(hot[v], min(pres[u], default = 0)))
    if isinf(dsts[t]):
        print('Impossible')
        return
    print(dsts[t], min(pres[t]))


if __name__ == '__main__':
    main()
