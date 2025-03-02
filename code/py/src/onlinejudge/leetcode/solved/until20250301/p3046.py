from onlinejudge.leetcode import *


class Solution:
    def isPossibleToSplit(self, nums: List[int]) -> bool:
        return all(cnt <= 2 for cnt in Counter(nums).values())
