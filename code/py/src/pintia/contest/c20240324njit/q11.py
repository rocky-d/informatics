from collections import deque
from functools import cache


def main() -> None:
    n, m = map(int, input().split())
    graph = [deque() for _ in range(1 + n)]
    for _ in range(m):
        s1, s2 = map(int, input().split())
        graph[s1].append(s2)
    a, b = map(int, input().split())

    seen = set()
    path = [0 for _ in range(1 + n)]
    path[b] = 1

    @cache
    def dfs(node: int) -> None:
        seen.add(node)
        if b != node:
            for nxt in graph[node]:
                dfs(nxt)
                path[node] += path[nxt]

    dfs(node = a)
    ans = str(path[a]) + ' '
    for i in range(1, 1 + n):
        if i in seen and 0 == path[i]:
            ans += 'No'
            break
    else:
        ans += 'Yes'
    print(ans)


if __name__ == '__main__':
    main()
