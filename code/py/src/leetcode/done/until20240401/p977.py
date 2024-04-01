from rockyutil.leetcode import *


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        ans = []
        lft, rit = 0, len(nums) - 1
        while lft <= rit:
            if abs(nums[rit]) < abs(nums[lft]):
                ans.insert(0, nums[lft] * nums[lft])
                lft += 1
            else:
                ans.insert(0, nums[rit] * nums[rit])
                rit -= 1
        return ans
