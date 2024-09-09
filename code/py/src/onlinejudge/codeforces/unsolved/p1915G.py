from heapq import heappop, heappush
from math import inf


def main() -> None:
    n, m = map(int, input().split())
    uvw = (map(int, input().split()) for _ in range(m))

    graph = [None] + [[] for _ in range(n)]
    for u, v, w in uvw:
        graph[u].append((v, w))
        graph[v].append((u, w))

    s = map(int, input().split())

    s = [None] + list(s)
    dsts = [None] + [[inf] * 1001 for _ in range(n)]
    dsts[1][s[1]] = 0
    heap = []
    heappush(heap, (dsts[1][s[1]], 1, s[1]))
    while 0 < len(heap):
        u_dst, u, u_s = heappop(heap)
        if u_dst != dsts[u][u_s]:
            continue
        for v, w in graph[u]:
            v_dst = u_dst + w * u_s
            v_s = min(u_s, s[v])
            if v_dst < dsts[v][v_s]:
                dsts[v][v_s] = v_dst
                heappush(heap, (v_dst, v, v_s))
    print(min(dsts[n]))


if __name__ == '__main__':
    for _ in range(int(input())):
        main()
