from rockyutil.leetcode import *


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        lft, rit = bisect_left(nums, target), bisect_right(nums, target)
        return [-1, -1] if lft == rit else [lft, rit - 1]
