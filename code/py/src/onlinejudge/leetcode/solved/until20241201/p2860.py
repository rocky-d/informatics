from onlinejudge.leetcode import *


class Solution:
    def countWays(self, nums: List[int]) -> int:
        return sum(1 for cnt, (lst, nxt) in enumerate(pairwise(chain([-inf], sorted(nums), [inf])), start=0) if lst < cnt < nxt)
