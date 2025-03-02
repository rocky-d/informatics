from onlinejudge.leetcode import *


class Solution:
    def minChanges(self, s: str) -> int:
        ans = 0
        addition = 0
        for _, group in groupby(s):
            if 0b0 == 0b1 & len(list(group)) + addition:
                addition = 0
            else:
                addition = 1
                ans += 1
        return ans
