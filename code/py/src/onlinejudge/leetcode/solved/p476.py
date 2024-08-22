from onlinejudge.leetcode import *


class Solution:
    def findComplement(self, num: int) -> int:
        return int(reduce(add, ('0' if '1' == bit else '1' for bit in bin(num)[2:])), base = 2)
