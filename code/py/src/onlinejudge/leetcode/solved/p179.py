from onlinejudge.leetcode import *


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums = sorted(map(str, nums), key=lambda x: x * 9, reverse=True)
        return '0' if '0' == nums[0] else ''.join(nums)
