from onlinejudge.leetcode import *


class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        ans = 0
        height = 0
        for diff in gain:
            height += diff
            ans = max(ans, height)
        return ans
