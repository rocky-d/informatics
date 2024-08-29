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

        rows, cols = defaultdict(lambda: []), defaultdict(lambda: [])
        for i, (xi, yi) in enumerate(stones):
            rows[xi].append(i)
            cols[yi].append(i)
        for ls in chain(rows.values(), cols.values()):
            for u, v in pairwise(ls):
                u_head, v_head = find(x=u), find(x=v)
                if u_head != v_head:
                    heads[u] = heads[u_head] = v_head
                    ans += 1
        return ans
