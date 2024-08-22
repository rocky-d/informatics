from onlinejudge.leetcode import *


class Solution:
    def bitwiseComplement(self, n: int) -> int:
        return int(reduce(add, ('0' if '1' == bit else '1' for bit in bin(n)[2:])), base = 2)
