from onlinejudge.leetcode import *


class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        heads = list(range(n))

        def find(x: int) -> int:
            if x == heads[x]:
                return x
            heads[x] = find(heads[x])
            return heads[x]

        for u, v in edges:
            u_head, v_head = find(x = u), find(x = v)
            if u_head != v_head:
                heads[u] = heads[u_head] = v_head
        return find(x = source) == find(x = destination)
