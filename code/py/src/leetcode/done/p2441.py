from rockyutil.leetcode import *


class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        nums.sort()
        lft, rit = 0, -1
        while nums[lft] ^ nums[rit] < 0:
            total = nums[lft] + nums[rit]
            if total < 0:
                lft += 1
            elif 0 < total:
                rit -= 1
            else:
                ans = nums[rit]
                break
        else:
            ans = -1
        return ans
