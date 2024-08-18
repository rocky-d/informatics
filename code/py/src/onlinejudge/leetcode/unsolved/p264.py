from onlinejudge.leetcode import *


class Solution:
    def nthUglyNumber(self, n: int) -> int:
        vis = {1}
        heap = [1]
        for i in range(1, n):
            num = heappop(heap)
            for factor in 2, 3, 5:
                nxt = num * factor
                if nxt in vis:
                    continue
                vis.add(nxt)
                heappush(heap, nxt)
        return heappop(heap)
