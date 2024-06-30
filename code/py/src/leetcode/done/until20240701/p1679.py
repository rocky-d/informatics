from rockyutil.leetcode import *


class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        ans = 0
        nums.sort()
        lft, rit = 0, len(nums) - 1
        while lft < rit:
            sum_ = nums[lft] + nums[rit]
            if k < sum_:
                rit -= 1
            elif sum_ < k:
                lft += 1
            else:
                ans += 1
                lft += 1
                rit -= 1
        return ans
