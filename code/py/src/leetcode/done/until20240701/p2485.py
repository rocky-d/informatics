from rockyutil.leetcode import *


class Solution:
    def pivotInteger(self, n: int) -> int:
        tmp = n * (n + 1) // 2
        x = isqrt(tmp)
        return x if x * x == tmp else -1
