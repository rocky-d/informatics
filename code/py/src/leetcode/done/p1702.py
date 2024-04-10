from rockyutil.leetcode import *


class Solution:
    def maximumBinaryString(self, binary: str) -> str:
        if '0' not in binary:
            return binary
        binary_groupby = groupby(binary)
        c, s = next(binary_groupby)
        idx = len(list(s)) - 1
        for c, s in binary_groupby:
            if '0' == c:
                idx += len(list(s))
        return '1' * idx + '0' + '1' * (len(binary) - idx - 1)
