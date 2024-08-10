from onlinejudge.leetcode import *


class Solution:
    def minRectanglesToCoverPoints(self, points: List[List[int]], w: int) -> int:
        ans = 0
        cover = -1
        for x in sorted(frozenset(x for x, y in points)):
            if cover < x:
                cover = x + w
                ans += 1
        return ans
