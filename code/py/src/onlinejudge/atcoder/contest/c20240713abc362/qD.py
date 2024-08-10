from heapq import heappop, heappush
from math import inf


def main() -> None:
    n, m = map(int, input().split())
    a = map(int, input().split())
    uvb = (map(int, input().split()) for _ in range(m))

    a = [None] + list(a)
    graph = [None] + [[] for _ in range(n)]
    for u, v, b in uvb:
        graph[u].append((v, b + a[v]))
        graph[v].append((u, b + a[u]))
    dsts = [None] + [inf] * n
    dsts[1] = a[1]
    heap = []
    heappush(heap, (dsts[1], 1))
    while 0 < len(heap):
        dst, node = heappop(heap)
        if dst != dsts[node]:  # if dst > dsts[node]:
            continue
        for nxt, cost in graph[node]:
            if dst + cost < dsts[nxt]:
                dsts[nxt] = dst + cost
                heappush(heap, (dsts[nxt], nxt))
    print(*dsts[2:])


if __name__ == '__main__':
    main()
