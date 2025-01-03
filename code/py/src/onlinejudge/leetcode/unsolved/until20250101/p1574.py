from onlinejudge.leetcode import *


class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        n = len(arr)

        def check(mid: int) -> bool:
            for i in range(n - mid + 1):
                ...

        lo, hi = -1, n
        while 1 < hi - lo:
            mid = lo + hi >> 1
            if check(mid=mid):
                lo = mid
            else:
                hi = mid
        return hi
