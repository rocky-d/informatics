from onlinejudge.leetcode import *


class Solution:
    def minimumCost(self, n: int, edges: List[List[int]], query: List[List[int]]) -> List[int]:
        ans = []
        heads = [node for node in range(n)]

        def find(node: int) -> int:
            if node == heads[node]:
                return node
            heads[node] = find(heads[node])
            return heads[node]

        weights = {node: -0b1 for node in range(n)}
        for u, v, w in edges:
            u_head, v_head = find(node = u), find(node = v)
            if u_head != v_head:
                heads[u] = heads[u_head] = v_head
                weights[v_head] &= weights.pop(u_head)
            weights[v_head] &= w
        for s, t in query:
            if s == t:
                ans.append(0)
            else:
                s_head, t_head = find(node = s), find(node = t)
                ans.append(weights[s_head] if s_head == t_head else -1)
        return ans
