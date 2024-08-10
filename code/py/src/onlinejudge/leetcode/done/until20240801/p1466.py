from onlinejudge.leetcode import *


class Solution:
    ans = 0

    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        nexts = [set() for _i in range(n)]
        children = [[] for _i in range(n)]
        for connection in connections:
            nexts[connection[0]].add(connection[1])
            children[connection[0]].append(connection[1])
            children[connection[1]].append(connection[0])

        def dfs(node: int, parent: int) -> None:
            for child in children[node]:
                if parent == child:
                    continue
                dfs(child, node)
                if child in nexts[node]:
                    self.ans += 1

        dfs(0, -1)
        return self.ans
