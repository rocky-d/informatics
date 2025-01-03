from onlinejudge.leetcode import *


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        maxm = max(nums)
        return max(len(list(group)) for num, group in groupby(nums) if num == maxm)
