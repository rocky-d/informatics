from onlinejudge.leetcode import *


class Solution:
    def maximumLength(self, s: str) -> int:
        def check(mid: int) -> bool:
            cnter = defaultdict(lambda: 0)
            for i in range(len(s) - mid + 1):
                s_sub = s[i : i + mid]
                if 1 != len(frozenset(s_sub)):
                    continue
                cnter[s_sub] += 1
                if 3 <= cnter[s_sub]:
                    res = True
                    break
            else:
                res = False
            return res

        lo, hi = 0, len(s) - 1
        while 1 < hi - lo:
            mid = lo + hi >> 1
            if check(mid):
                lo = mid
            else:
                hi = mid
        return -1 if 0 == lo else lo
