from onlinejudge.leetcode import *


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        heads = list(range(n))

        def find(x: int) -> int:
            if x == heads[x]:
                return x
            heads[x] = find(heads[x])
            return heads[x]

        for u, row in enumerate(isConnected):
            for v in range(u + 1, n):
                if 1 == row[v]:
                    u_head, v_head = find(x = u), find(x = v)
                    if u_head != v_head:
                        heads[u] = heads[u_head] = v_head
        return len(frozenset(find(x = x_head) for x_head in heads))
