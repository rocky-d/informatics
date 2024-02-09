from rockyutil.leetcode import *


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left, right = bisect_left(nums, target), bisect_right(nums, target)
        return [-1, -1] if left == right else [left, right - 1]
