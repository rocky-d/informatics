from onlinejudge.leetcode import *


class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        return abs(sum(nums) - sum(map(int, reduce(add, map(str, nums)))))
