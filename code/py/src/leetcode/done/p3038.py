from rockyutil.leetcode import *


class Solution:
    def maxOperations(self, nums: List[int]) -> int:
        ans = 1
        val = nums[0] + nums[1]
        for i in range(3, len(nums), 2):
            if val == nums[i - 1] + nums[i]:
                ans += 1
            else:
                break
        return ans
