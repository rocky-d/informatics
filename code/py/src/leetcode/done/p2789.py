from rockyutil.leetcode import *


class Solution:
    def maxArrayValue(self, nums: List[int]) -> int:
        ans = nums[0]
        p = len(nums) - 1
        while 0 < p:
            val = nums[p]
            p -= 1
            while 0 <= p and nums[p] <= val:
                val += nums[p]
                p -= 1
            ans = max(ans, val)
        return ans
