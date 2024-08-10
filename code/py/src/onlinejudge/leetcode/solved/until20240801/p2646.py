from onlinejudge.leetcode import *


class Solution:
    def minimumTotalPrice(self, n: int, edges: List[List[int]], price: List[int], trips: List[List[int]]) -> int:
        children = [[] for _i in range(n)]
        for edge in edges:
            children[edge[0]].append(edge[1])
            children[edge[1]].append(edge[0])

        def dfs(node: int, parent: int, target: int) -> bool:
            if target == node:
                count[node] += 1
                return True
            for child in children[node]:
                if parent == child:
                    continue
                if dfs(child, node, target):
                    count[node] += 1
                    return True
            return False

        count = [0 for _i in range(n)]
        for start, end in trips:
            dfs(node = start, parent = -1, target = end)

        def dp(node: int, parent: int) -> Tuple[int, int]:
            res = price[node] * count[node], price[node] * count[node] // 2
            for child in children[node]:
                if parent == child:
                    continue
                whole, half = dp(node = child, parent = node)
                res = res[0] + min(whole, half), res[1] + whole
            return res

        return min(dp(node = 0, parent = -1))
