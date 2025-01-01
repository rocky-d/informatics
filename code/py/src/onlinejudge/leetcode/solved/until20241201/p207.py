from onlinejudge.leetcode import *


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]
        ins = [0] * numCourses
        for v, u in prerequisites:
            graph[u].append(v)
            ins[v] += 1
        nodes = 0
        que = deque(node for node in range(numCourses) if 0 == ins[node])
        while 0 < len(que):
            nodes += 1
            node = que.pop()
            for nxt in graph[node]:
                ins[nxt] -= 1
                if 0 == ins[nxt]:
                    que.append(nxt)
        return numCourses == nodes
