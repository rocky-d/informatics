from onlinejudge.leetcode import *


class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        ans = maxm = 0
        for idx, val in enumerate(values):
            maxm_lst, maxm = maxm, max(maxm, val + idx)
            ans = max(ans, maxm_lst + val - idx)
        return ans
