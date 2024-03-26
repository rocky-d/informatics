from rockyutil.leetcode import *


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums_set = frozenset(nums)
        for num in range(1, len(nums) + 1):
            if num not in nums_set:
                ans = num
                break
        else:
            ans = len(nums) + 1
        return ans
