def main() -> None:
    n, m = map(int, input().split())
    edges = (map(int, input().split()) for _ in range(m))

    ans = 0
    graph = [None] + [[] for _ in range(n)]
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    def dfs(u: int, seen: int, cnt: int) -> None:
        nonlocal ans
        cnt += 1
        ans = max(ans, cnt)
        vs = [v for v in graph[u] if 0b0 == 0b1 << v & seen]
        for v in vs:
            seen |= 0b1 << v
        for v in vs:
            dfs(v, seen, cnt)

    for start in range(1, 1 + n):
        dfs(u = start, seen = 0b1 << start, cnt = 0)
    print(ans)


if __name__ == '__main__':
    main()
