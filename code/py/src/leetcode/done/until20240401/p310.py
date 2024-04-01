from rockyutil.leetcode import *


class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(n)]
        ins = Counter()
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
            ins[a] += 1
            ins[b] += 1
        que_lst, que = [0], [fr for fr, in_ in ins.items() if 1 == in_]
        while 0 < len(que):
            que_lst, que = que, []
            for fr in que_lst:
                for to in graph[fr]:
                    ins[to] -= 1
                    if 1 == ins[to]:
                        que.append(to)
        return que_lst


eg_n = 6
eg_edges = [[3, 0], [3, 1], [3, 2], [3, 4], [5, 4]]
print(Solution().findMinHeightTrees(eg_n, eg_edges))
