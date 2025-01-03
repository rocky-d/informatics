from onlinejudge.leetcode import *


class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        lo, hi = min(start, destination), max(start, destination)
        return min(sum(distance[lo:hi]), sum(distance[:lo]) + sum(distance[hi:]))
