from onlinejudge.leetcode import *


class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        return abs(sum(nums) - sum(sum(map(int, str(num))) for num in nums))
