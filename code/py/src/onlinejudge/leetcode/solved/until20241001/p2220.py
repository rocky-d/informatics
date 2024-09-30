from onlinejudge.leetcode import *


class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        return sum(1 for bit1, bit2 in zip_longest(bin(start)[:1:-1], bin(goal)[:1:-1], fillvalue='0') if bit1 != bit2)
