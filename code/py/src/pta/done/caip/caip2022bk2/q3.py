from collections import deque
from heapq import heappush, heappop
from math import inf


def main() -> None:
    n, m, k, p = map(int, input().split())
    pi = map(int, input().split())
    uv = (map(int, input().split()) for _ in range(m))

    pi = [None] + list(pi)
    graph = [None] + [[] for _ in range(n)]
    for u, v in uv:
        graph[u].append(v)
        graph[v].append(u)

    s, t = map(int, input().split())

    ans = 0
    dsts = [None] + [inf] * n
    dsts[s] = 0
    pres = [None] + [[] for _ in range(n)]
    heap = []
    heappush(heap, (dsts[s], s))
    while 0 < len(heap):
        dst, u = heappop(heap)
        if dst != dsts[u]:
            continue
        dst1 = dst + 1
        for v in graph[u]:
            if dst1 < dsts[v]:
                dsts[v] = dst1
                pres[v] = [u]
                heappush(heap, (dst1, v))
            elif dst1 == dsts[v]:
                pres[v].append(u)
    que = deque([(t, deque())])
    while 0 < len(que):
        u, stk = que.popleft()
        stk.appendleft(pi[u])
        if s == u:
            ans = max(ans, sum(list(stk)[p - 1::k]))
        else:
            for v in pres[u]:
                que.append((v, deque(stk)))
    print(ans)


if __name__ == '__main__':
    main()
