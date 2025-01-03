from onlinejudge.leetcode import *


class Solution:
    def maximumBinaryString(self, binary: str) -> str:
        binary_groupby = groupby(binary)
        c, s = next(binary_groupby)
        any_zero = '0' == c
        idx = len(list(s)) - 1
        for c, s in binary_groupby:
            if '0' == c:
                any_zero = True
                idx += len(list(s))
        return '1' * idx + '0' + '1' * (len(binary) - idx - 1) if any_zero else binary
