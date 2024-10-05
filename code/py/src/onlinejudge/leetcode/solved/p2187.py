from onlinejudge.leetcode import *


class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        return 1 + bisect_left(range(1, 1 + min(time) * totalTrips), 1, key=lambda mid: 1 if totalTrips <= sum(mid // t for t in time) else 0)
