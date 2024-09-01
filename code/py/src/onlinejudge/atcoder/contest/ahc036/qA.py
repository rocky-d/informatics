import sys

dir = 'C:/rocky_d/code/informatics/code/py/src/onlinejudge/atcoder/contest/ahc036/'
sys.stdin = open(dir + 'in.txt', 'r')
sys.stdout = open(dir + 'out.txt', 'w')


from collections import Counter
from heapq import heappop, heappush
from itertools import chain, pairwise


def main() -> None:
    n, m, _, la, lb = map(int, input().split())

    a = list(range(n)) + list(range(la - n))
    print(*a)
    lb_l, lb_r = 1, lb - 1

    uv = (map(int, input().split()) for _ in range(m))

    graph = [[] for _ in range(n)]
    for fr, to in uv:
        graph[fr].append(to)
        graph[to].append(fr)

    t = map(int, input().split())
    # xy = (map(int, input().split()) for _ in range(n))

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
    # sm = []
    excludes = frozenset(x for x, _ in sorted(Counter(route).items(), key=lambda item:item[1], reverse=True)[:lb_r])
    for pb, pa in enumerate(excludes, start=lb - len(excludes)):
        # sm.append(f"s {1} {pa} {pb}")
        print('s', 1, pa, pb)
    idx = len(route) - 1
    while 0 <= idx:
        idx_lst = idx
        while 0 <= idx and route[idx] in excludes:
            idx -= 1
        if not 0 <= idx:
            break
        lo, hi = route[idx], route[idx]
        lo_lst, hi_lst = lo, hi
        idx -= 1
        while 0 <= idx and hi - lo < lb_l:
            while 0 <= idx and route[idx] in excludes:
                idx -= 1
            if not 0 <= idx:
                break
            if route[idx] < lo:
                lo_lst, hi_lst = lo, hi
                lo = route[idx]
            elif hi < route[idx]:
                lo_lst, hi_lst = lo, hi
                hi = route[idx]
            idx -= 1
        if not hi - lo < lb_l:
            lo, hi = lo_lst, hi_lst
            idx += 1
        hi += 1
        # sm.append(f"s {hi - lo} {lo} {0}")
        print('s', hi - lo, lo, 0)
        for i in range(idx_lst, idx, -1):
            # sm.append(f"m {route[i]}")
            print('m', route[i])
    # print(*sm, sep='\n')


if __name__ == '__main__':
    main()
