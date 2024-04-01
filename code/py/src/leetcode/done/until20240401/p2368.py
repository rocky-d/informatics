from rockyutil.leetcode import *


class Solution:
    def reachableNodes(self, n: int, edges: List[List[int]], restricted: List[int]) -> int:
        ans = 1
        graph = [[] for _ in range(n)]
        for a, b in edges:
            graph[a].append(b), graph[b].append(a)
        seen = {0} | set(restricted)
        que = deque((0,))
        while 0 < len(que):
            for nxt in graph[que.popleft()]:
                if nxt not in seen:
                    seen.add(nxt)
                    que.append(nxt)
                    ans += 1
        return ans
