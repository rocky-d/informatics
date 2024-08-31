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

    ans = []
    a = list(range(n)) + [0] * (la - n)
    ans.append(' '.join(map(str, a)))

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
        for x in reversed(route):
            ans.append(f"s 1 {x} 0")
            ans.append(f"m {x}")
    print(*ans, sep='\n')


if __name__ == '__main__':
    main()
