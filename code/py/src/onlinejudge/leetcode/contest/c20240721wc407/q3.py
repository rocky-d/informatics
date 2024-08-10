from onlinejudge.leetcode import *


class Solution:
    def maxOperations(self, s: str) -> int:
        ans = 0
        ones = 0
        for char, group in groupby(s):
            if '0' == char:
                ans += ones
            else:
                ones += len(list(group))
        return ans
