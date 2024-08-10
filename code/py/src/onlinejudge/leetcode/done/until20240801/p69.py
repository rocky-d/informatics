from onlinejudge.leetcode import *


class Solution:
    def mySqrt(self, x: int) -> int:
        return bisect_right(range(x + 1), x, key = lambda i: i * i) - 1
