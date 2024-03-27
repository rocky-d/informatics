from rockyutil.leetcode import *


class Solution:
    def countWays(self, ranges: List[List[int]]) -> int:
        ranges.sort(key = lambda rang: (rang[0], rang[1]))
        groups = 0
        rit_max = -1
        for lft, rit in ranges:
            if rit_max < lft:
                groups += 1
            rit_max = max(rit_max, rit)
        return (0b1 << groups) % 1_000_000_007
