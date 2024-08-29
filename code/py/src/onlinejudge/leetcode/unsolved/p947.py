from onlinejudge.leetcode import *


class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        ans = 0
        heads = list(range(len(stones)))

        def find(x: int) -> int:
            if x == heads[x]:
                return x
            heads[x] = find(heads[x])
            return heads[x]

        rows, cols = {}, {}
        for u, (xi, yi) in enumerate(stones):
            if xi in rows.keys():
                v = rows[xi]
                u_head, v_head = find(x=u), find(x=v)
                if u_head != v_head:
                    heads[u] = heads[u_head] = v_head
                    ans += 1
            else:
                rows[xi] = u
            if yi in cols.keys():
                v = cols[yi]
                u_head, v_head = find(x=u), find(x=v)
                if u_head != v_head:
                    heads[u] = heads[u_head] = v_head
                    ans += 1
            else:
                cols[yi] = u
        return ans
