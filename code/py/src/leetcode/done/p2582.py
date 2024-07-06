from rockyutil.leetcode import *


class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        quotient, remainder = divmod(time, n - 1)
        return 1 + remainder if 0b0 == 0b1 & quotient else n - remainder
