from onlinejudge.leetcode import *


class Solution:
    def evenOddBit(self, n: int) -> List[int]:
        ans = [0, 0]
        for idx, digit in enumerate(bin(n)[:1:-1]):
            if '0' == digit:
                continue
            ans[0b1 & idx] += 1
        return ans
