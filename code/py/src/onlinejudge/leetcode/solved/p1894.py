from onlinejudge.leetcode import *


class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        k %= sum(chalk)
        for idx, num in enumerate(chalk):
            if k < num:
                ans = idx
                break
            k -= num
        return ans
