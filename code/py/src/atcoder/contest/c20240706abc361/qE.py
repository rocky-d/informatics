from collections import deque
from typing import List


def main() -> None:
    n = int(input())
    edges = (map(int, input().split()) for _ in range(n - 1))

    ans = 0

    class NaryTreeNode(object):
        def __init__(self, val: int, nxts: List['NaryTreeNode']) -> None:
            self.val = val
            self.nxts = nxts

    nodes = [None] + [NaryTreeNode(val = i, nxts = []) for i in range(1, 1 + n)]
    graph = [None] + [{} for _ in range(1, 1 + n)]
    for a, b, c in edges:
        graph[a][b] = graph[b][a] = c
        ans += c + c
    seen = [None] + [False] * n
    que = deque(i for i in range(1, 1 + n) if 1 == len(graph[i]))
    while 0 < len(que):
        i = que.popleft()
        seen[i] = True
        for nb in graph[i].keys():
            if seen[nb] is True:
                continue
            nodes[nb].nxts.append(nodes[i])
            que.append(nb)
    root = nodes[i]
    maxm = 0

    def dfs(node: NaryTreeNode) -> int:
        nonlocal maxm
        dsts = [0, 0]
        for nxt in node.nxts:
            dst = dfs(nxt) + graph[node.val][nxt.val]
            if dsts[0] < dst:
                dsts[0], dsts[1] = dst, dsts[0]
            elif dsts[1] < dst:
                dsts[1] = dst
        maxm = max(maxm, dsts[0] + dsts[1])
        return dsts[0]

    dfs(node = root)
    ans -= maxm
    print(ans)


if __name__ == '__main__':
    main()
