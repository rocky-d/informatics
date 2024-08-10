from onlinejudge.leetcode import *


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        idx = bisect_right(nums, target) - 1
        return idx if nums[idx] == target else -1
