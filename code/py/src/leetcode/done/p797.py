from rockyutil.leetcode import *


class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        ans = []
        stk = deque()
        n = len(graph)

        def dfs(node: int) -> None:
            stk.append(node)
            if node == n - 1:
                ans.append(list(stk))
            else:
                for nxt in graph[node]:
                    dfs(nxt)
            stk.pop()

        dfs(node = 0)
        return ans
