from onlinejudge.leetcode import *


class Solution:
    def find(self, uf: List[int], i: int) -> int:
        if uf[i] == i:
            return i
        uf[i] = self.find(uf, uf[i])
        return uf[i]

    def minOperationsQueries(self, n: int, edges: List[List[int]], queries: List[List[int]]) -> List[int]:
        m, w = len(queries), 26
        neighbors = [dict() for _ in range(n)]
        for edge in edges:
            neighbors[edge[0]][edge[1]] = edge[2]
            neighbors[edge[1]][edge[0]] = edge[2]
        queryArr = [[] for _ in range(n)]
        for i in range(m):
            queryArr[queries[i][0]].append([queries[i][1], i])
            queryArr[queries[i][1]].append([queries[i][0], i])

        count = [[0 for _ in range(w + 1)] for _ in range(n)]
        visited, uf, lca = [0 for _ in range(n)], [0 for _ in range(n)], [0 for _ in range(m)]

        def tarjan(node: int, parent: int):
            if parent != -1:
                count[node] = count[parent].copy()
                count[node][neighbors[node][parent]] += 1
            uf[node] = node
            for child in neighbors[node].keys():
                if child == parent:
                    continue
                tarjan(child, node)
                uf[child] = node
            for [node1, index] in queryArr[node]:
                if node != node1 and not visited[node1]:
                    continue
                lca[index] = self.find(uf, node1)
            visited[node] = 1

        tarjan(0, -1)
        ans = [0 for i in range(m)]
        for i in range(m):
            totalCount, maxCount = 0, 0
            for j in range(1, w + 1):
                t = count[queries[i][0]][j] + count[queries[i][1]][j] - 2 * count[lca[i]][j]
                maxCount = max(maxCount, t)
                totalCount += t
            ans[i] = totalCount - maxCount
        return ans
