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

    dsts = [None] + [inf] * n
    dsts[1] = 0
    ss = [None] + [inf] * n
    ss[1] = s[1]
    heap = []
    heappush(heap, (dsts[1], ss[1], 1))
    for _ in range(5000):
        if 0 == len(heap):
            break
        u_dst, u_s, u = heappop(heap)
        if u_dst != dsts[u] and u_s != ss[u]:
            continue
        for v, w in graph[u]:
            v_dst = u_dst + w * u_s
            v_s = min(u_s, s[v])
            if v_dst < dsts[v] or v_s < u_s or v_s < ss[v]:
                heappush(heap, (v_dst, v_s, v))
                dsts[v] = min(dsts[v], v_dst)
                ss[v] = min(ss[v], v_s)
    print(dsts[n])


if __name__ == '__main__':
    for _ in range(int(input())):
        main()
