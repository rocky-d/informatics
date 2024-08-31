from collections import deque
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

    def dfs(u: int) -> bool:
        if u == to:
            return True
        for v in graph[u]:
            if vis[v]:
                continue
            vis[v] = True
            stk.append(v)
            if dfs(v):
                res = True
                break
            stk.pop()
            vis[v] = False
        else:
            res = False
        return res

    for fr, to in pairwise(chain([0], t)):
        stk = deque()
        vis = [False] * n
        vis[fr] = True
        dfs(u=fr)
        for x in stk:
            ans.append(f"s 1 {x} 0")
            ans.append(f"m {x}")
    print(*ans, sep='\n')


if __name__ == '__main__':
    main()
