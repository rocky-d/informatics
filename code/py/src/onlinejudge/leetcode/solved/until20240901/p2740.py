from onlinejudge.leetcode import *


class Solution:
    def findValueOfPartition(self, nums: List[int]) -> int:
        return min(nxt - lst for lst, nxt in pairwise(sorted(nums)))
