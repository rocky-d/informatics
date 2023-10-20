from rockyutil.leetcode import *


class Solution:
    def rob(self, nums: List[int]) -> int:
        first, second = 0, 0
        for num in nums:
            first, second = second, max(second, first + num)
        return second
