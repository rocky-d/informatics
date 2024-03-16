from collections import deque, defaultdict, Counter


def main() -> None:
    n, m = map(int, input().split())
    nodes = set()
    graph = defaultdict(lambda: deque())
    ins = Counter()
    for _ in range(m):
        u, v, w = map(int, input().split())
        nodes.add(u)
        nodes.add(v)
        graph[u].append((v, w))
        ins[v] += 1
    starts = graph.keys() - ins.keys()
    que = [u for u in starts]  # 筛选入度为0的顶点
    cnt = 0
    while que:
        u = que.pop()
        cnt += 1
        for v, w in graph[u]:
            ins[v] -= 1
            if ins[v] == 0:
                que.append(v)
    if cnt < len(nodes):
        print('NOWAY')
        return

    def dfs(u, nodes, total):
        if ans[0] < nodes:
            ans[0] = nodes
            ans[1] = total
        elif ans[0] == nodes and total >= ans[1]:
            ans[1] = total
        for v, w in graph[u]:
            if v not in seen:
                seen.add(v)
                dfs(v, nodes + 1, total + w)
                seen.remove(v)

    ans = [0, 0]
    seen = set()
    for start in starts:
        seen.clear()
        # dfs(start, 1, 0)
        seen.add(start)
        que = deque(((start, 1, 0),))
        while 0 < len(que):
            u, nodes, total = que.popleft()
            if total > ans[1]:
                ans[1] = total
            for v, w in graph[u]:
                if v not in seen:
                    seen.add(v)
                    que.append((v, nodes + 1, total + w))
    print(ans[1])


if __name__ == '__main__':
    main()
