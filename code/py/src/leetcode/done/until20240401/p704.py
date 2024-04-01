from rockyutil.leetcode import *


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        index = bisect_right(nums, target) - 1
        return index if nums[index] == target else -1
