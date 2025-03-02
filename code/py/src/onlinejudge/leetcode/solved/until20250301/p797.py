from onlinejudge.leetcode import *


class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        ans = []
        stk = deque()
        dest = len(graph) - 1

        def dfs(node: int) -> None:
            stk.append(node)
            if dest == node:
                ans.append(list(stk))
            else:
                for nxt in graph[node]:
                    dfs(nxt)
            stk.pop()

        dfs(node = 0)
        return ans
