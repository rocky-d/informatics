from heapq import heappop, heappush
from math import inf


def main() -> None:
    n, m, s = map(int, input().split())
    graph = [[] for _ in range(1 + n)]
    for _ in range(m):
        u, v, w = map(int, input().split())
        graph[u].append((v, w))

    dsts = [inf] * (1 + n)
    dsts[s] = 0
    heap = []
    heappush(heap, (dsts[s], s))
    while 0 < len(heap):
        dst, node = heappop(heap)
        if dst > dsts[node]:
            continue
        for nxt, cost in graph[node]:
            if dst + cost < dsts[nxt]:
                dsts[nxt] = dst + cost
                heappush(heap, (dsts[nxt], nxt))
    print(*dsts[1:])


if __name__ == '__main__':
    main()
