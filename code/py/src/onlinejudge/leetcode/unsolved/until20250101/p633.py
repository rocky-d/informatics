from onlinejudge.leetcode import *


class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        a, b = 0, isqrt(c)
        while a <= b:
            aabb = a * a + b * b
            if aabb < c:
                a += 1
            elif c < aabb:
                b -= 1
            else:
                ans = True
                break
        else:
            ans = False
        return ans
