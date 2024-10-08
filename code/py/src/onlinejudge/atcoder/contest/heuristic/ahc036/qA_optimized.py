import sys

dir = 'C:/rocky_d/code/informatics/code/py/src/onlinejudge/atcoder/contest/ahc036/'
sys.stdin = open(dir + 'in.txt', 'r')
sys.stdout = open(dir + 'out_optimized.txt', 'w')


from collections import Counter
from heapq import heappop, heappush
from itertools import chain, pairwise


def main() -> None:
    n, m, _, la, lb = map(int, input().split())

    a = list(range(n)) + list(range(la - n))
    print(*a)

    uv = (map(int, input().split()) for _ in range(m))

    graph = [[] for _ in range(n)]
    for fr, to in uv:
        graph[fr].append(to)
        graph[to].append(fr)

    t = map(int, input().split())

    route = []
    for fr, to in pairwise(chain([0], t)):
        n = len(graph)
        dsts = [n] * n
        dsts[fr] = 0
        lsts = [None] * n
        heap = []
        heappush(heap, (dsts[fr], fr))
        while 0 < len(heap):
            u_dst, u = heappop(heap)
            if u_dst != dsts[u]:  # if u_dst > dsts[u]:
                continue
            if u == to:
                break
            for v in graph[u]:
                v_dst = u_dst + 1
                if v_dst < dsts[v]:
                    heappush(heap, (v_dst, v))
                    dsts[v] = v_dst
                    lsts[v] = u
                elif v_dst == dsts[v]:
                    lsts[v] = min(lsts[v], u, key=lambda x: abs(x - v))
        ls = []
        x = to
        while fr != x:
            ls.append(x)
            x = lsts[x]
        ls += route
        route = ls
    excludes = frozenset(x for x, _ in sorted(Counter(route).items(), key=lambda item: item[1], reverse=True)[: lb - 1])
    for pb, pa in enumerate(excludes, start=1):
        print('s', 1, pa, pb)
    for x in reversed(route):
        if x not in excludes:
            print('s', 1, x, 0)
        print('m', x)


if __name__ == '__main__':
    main()
