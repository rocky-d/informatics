import sys

dir = 'C:/rocky_d/code/informatics/code/py/src/onlinejudge/atcoder/contest/ahc036/'
sys.stdin = open('in.txt', 'r')
sys.stdout = open('out.txt', 'w')


from heapq import heappop, heappush
from itertools import chain, pairwise


def main() -> None:
    n, m, _, la, lb = map(int, input().split())
    uv = (map(int, input().split()) for _ in range(m))

    graph = [[] for _ in range(n)]
    for fr, to in uv:
        graph[fr].append(to)
        graph[to].append(fr)

    t = map(int, input().split())
    # xy = (map(int, input().split()) for _ in range(n))

    a = list(range(n)) + list(range(la - n))
    print(*a)
    # sm = []
    for fr, to in pairwise(chain([0], t)):
        n = len(graph)
        dsts = [n] * n
        dsts[fr] = 0
        pres = [None] * n
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
                    pres[v] = u
                elif v_dst == dsts[v]:
                    pres[v] = min(pres[v], u, key=lambda x: abs(x - fr))
        route = []
        x = to
        while fr != x:
            route.append(x)
            x = pres[x]
        idx = len(route) - 1
        while 0 <= idx:
            idx_lst = idx
            lo, hi = route[idx], route[idx]
            lo_lst, hi_lst = lo, hi
            idx -= 1
            while 0 <= idx and hi - lo < lb:
                if route[idx] < lo:
                    lo_lst, hi_lst = lo, hi
                    lo = route[idx]
                elif hi < route[idx]:
                    lo_lst, hi_lst = lo, hi
                    hi = route[idx]
                idx -= 1
            if not hi - lo < lb:
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
