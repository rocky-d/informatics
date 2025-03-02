from onlinejudge.leetcode import *


class Solution:
    def minOperations(self, k: int) -> int:
        k_isqrt = isqrt(k)
        return k_isqrt + ceil(k / k_isqrt) - 2
