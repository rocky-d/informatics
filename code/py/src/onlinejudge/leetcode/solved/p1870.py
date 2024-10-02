from onlinejudge.leetcode import *


class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        if hour <= len(dist) - 1:
            return -1
        dst_lst = dist.pop(-1)
        return 1 + bisect_left(range(1, 10_000_001), 1, key=lambda mid: 1 if sum((dst + mid - 1) // mid for dst in dist) + dst_lst / mid <= hour else 0)
