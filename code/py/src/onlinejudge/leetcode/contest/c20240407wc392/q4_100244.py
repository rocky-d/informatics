from onlinejudge.leetcode import *


class Solution:
    def minimumCost(self, n: int, edges: List[List[int]], query: List[List[int]]) -> List[int]:
        ans = []
        heads = [node for node in range(n)]
        groups = {node: [] for node in range(n)}

        def find(a: int) -> int:
            if a == heads[a]:
                return a
            heads[a] = find(heads[a])
            return heads[a]

        def union(a: int, b: int) -> None:
            a_head, b_head = find(a = a), find(a = b)
            if a_head != b_head:
                heads[a] = heads[a_head] = b_head
                groups[b_head] += groups.pop(a_head)
            groups[b_head].append(w)

        for u, v, w in edges:
            union(a = u, b = v)
        weights = {node: reduce(lambda x, y: x & y, group, 0b1111111111111111) for node, group in groups.items()}
        for s, t in query:
            if s == t:
                ans.append(0)
            else:
                s_head, t_head = find(a = s), find(a = t)
                if s_head == t_head:
                    ans.append(weights[s_head])
                else:
                    ans.append(-1)
        return ans


eg_n = 9
eg_edges = [[0, 4, 7], [3, 5, 1], [1, 3, 5], [1, 5, 1]]
eg_query = [[0, 4], [1, 5], [3, 0], [3, 3], [3, 2], [2, 0], [7, 7], [7, 0]]
print(Solution().minimumCost(eg_n, eg_edges, eg_query))
