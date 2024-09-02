from onlinejudge.leetcode import *


class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        prefs = list(accumulate(chalk))
        return bisect_right(prefs, k % prefs[-1])
