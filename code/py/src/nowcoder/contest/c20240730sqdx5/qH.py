def main() -> None:
    n, m = map(int, input().split())
    edges = (map(int, input().split()) for _ in range(m))

    ans = 0
    graph = [None] + [[] for _ in range(n)]
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    def dfs(u: int, cnt: int) -> None:
        nonlocal ans
        cnt += 1
        ans = max(ans, cnt)
        vs = [v for v in graph[u] if not seen[v]]
        for v in vs:
            seen[v] = True
        for v in vs:
            dfs(v, cnt)
        for v in vs:
            seen[v] = False

    for start in range(1, 1 + n):
        seen = [None] + [False] * n
        seen[start] = True
        dfs(u = start, cnt = 0)
        seen[start] = False
    print(ans)


if __name__ == '__main__':
    main()
