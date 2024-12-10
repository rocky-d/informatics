from onlinejudge.leetcode import *


class Solution:
    def maximumLength(self, s: str) -> int:
        def func(mid: int) -> int:
            cnter = defaultdict(lambda: 0)
            for i in range(len(s) - mid + 1):
                s_sub = s[i : i + mid]
                if 1 != len(frozenset(s_sub)):
                    continue
                cnter[s_sub] += 1
                if 3 <= cnter[s_sub]:
                    res = 0
                    break
            else:
                res = 1
            return res

        lo = bisect_left(range(1, len(s) - 1), 1, key=lambda mid: func(mid=mid))
        return -1 if 0 == lo else lo
