from rockyutil.leetcode import *


class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        ans = 0
        n = len(nums)
        line = nums[k]
        lft, rit = k - 1, k + 1
        while True:
            while 0 <= lft and line <= nums[lft]:
                lft -= 1
            while rit < n and line <= nums[rit]:
                rit += 1
            ans = max(ans, line * (rit - lft - 1))
            if 0 <= lft and rit < n:
                line = max(nums[lft], nums[rit])
            elif 0 <= lft:
                line = nums[lft]
            elif rit < n:
                line = nums[rit]
            else:
                break
        return ans
