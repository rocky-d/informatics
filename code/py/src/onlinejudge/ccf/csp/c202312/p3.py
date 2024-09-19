from collections import deque
from heapq import heapify, heappop


def main() -> None:
    n, m = map(int, input().split())
    w = map(int, input().split())
    p = map(int, input().split())
    q = (int(input()) for _ in range(m))

    ans = []
    w = list(w)
    total = sum(w)
    w = [None] + w
    p = list(p)
    ins = [None] + [0] * n
    for pi in p:
        ins[pi] += 1
    # ins_copy = ins.copy()
    p = [None] + [None] + p
    children = [None] + [{x} for x in range(1, 1 + n)]
    que = deque(i for i in range(1, 1 + n) if 0 == ins[i])
    while 0 < len(que):
        u = que.popleft()
        v = p[u]
        if v is None:
            continue
        w[v] += w[u]
        children[v].add(u)
        ins[v] -= 1
        if 0 == ins[v]:
            que.append(v)
    for i in range(1, 1 + n):
        w[i] = abs(total - w[i] - w[i])
    # jumps = [None] + [(i, w[i]) for i in range(1, 1 + n)]
    # ins = ins_copy
    # que = deque((i, w[i]) for i in range(1, 1 + n) if 0 == ins[i])
    # while 0 < len(que):
    #     u, u_w = que.popleft()
    #     v = p[u]
    #     if v is None:
    #         continue
    #     if u_w < jumps[v][1]:
    #         jumps[v] = u, u_w
    #     ins[v] -= 1
    #     if 0 == ins[v]:
    #         que.append((v, w[v]))
    # print(jumps)
    heap = [(w[i], i) for i in range(1, 1 + n)]
    heapify(heap)
    heap_copy = heap
    for qi in q:
        res = []
        vis = set()
        heap = heap_copy.copy()
        while True:
            breakpoint()
            while heap[0][1] in vis:
                heappop(heap)
            x = heap[0][1]
            res.append(x)
            if qi == x:
                break
            if qi in children[x]:
                for i in range(1, 1 + n):
                    if i in children[x]:
                        continue
                    vis.add(i)
            else:
                vis |= children[x]
        ans.append(' '.join(res))
        print(res)
    print(*ans, sep='\n')


if __name__ == '__main__':
    main()
