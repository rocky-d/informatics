from onlinejudge.leetcode import *


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        operations = 0
        lft = 0
        while lft + 2 < len(nums):
            if 0 == nums[lft]:
                operations += 1
                for i in range(3):
                    nums[lft + i] = ~nums[lft + i] + 2
            lft += 1
        return -1 if 0 in nums else operations
