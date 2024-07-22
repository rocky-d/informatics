from rockyutil.leetcode import *


class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        n = len(bombs)
        graph = [[] for _ in bombs]
        for (u, a), (v, b) in combinations(enumerate(bombs), 2):
            dst = (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2
            if dst <= a[2] ** 2:
                graph[u].append(v)
            if dst <= b[2] ** 2:
                graph[v].append(u)

        def bfs(start: int) -> int:
            res = 1
            seen = [False] * start + [True] + [False] * (n - start - 1)
            que = deque([start])
            while 0 < len(que):
                u = que.popleft()
                for v in graph[u]:
                    if seen[v]:
                        continue
                    seen[v] = True
                    que.append(v)
                    res += 1
            return res

        return max(bfs(start = x) for x in range(n))
