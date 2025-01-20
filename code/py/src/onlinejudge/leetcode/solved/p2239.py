from onlinejudge.leetcode import *


class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        return min(nums, key=lambda num: (abs(num - 0), -num))
