from onlinejudge.leetcode import *


class Solution:
    def nonSpecialCount(self, l: int, r: int) -> int:
        ans = r - l + 1
        n = isqrt(r) + 1
        tags = [False] * 2 + [True] * n
        for num in range(2, n):
            if tags[num]:
                if l <= num * num <= r:
                    ans -= 1
                for composite in range(num * num, n, num):
                    tags[composite] = False
        return ans
