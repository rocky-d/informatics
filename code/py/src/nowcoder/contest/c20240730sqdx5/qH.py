from functools import lru_cache


def main() -> None:
    n, m = map(int, input().split())
    edges = (map(int, input().split()) for _ in range(m))

    graph = [None] + [[] for _ in range(n)]
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    @lru_cache(maxsize = None)
    def dfs(cnt: int, u: int, seen: int) -> int:
        cnt += 1
        v_ls = [v for v in graph[u] if 0b0 == 0b1 << v & seen]
        for v in v_ls:
            seen |= 0b1 << v
        return max(cnt, max((dfs(cnt, v, seen) for v in v_ls), default = cnt))

    print(max(dfs(cnt = 0, u = start, seen = 0b1 << start) for start in range(1, 1 + n)))


if __name__ == '__main__':
    main()
