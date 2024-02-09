from rockyutil.leetcode import *


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        return [bisect_left(nums, target), bisect_right(nums, target) - 1] if target in nums else [-1, -1]
