from rockyutil.leetcode import *


class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        ans = 0
        n = len(nums)
        lft, rit = k, k
        for line in range(nums[k], 0, -1):
            while 0 <= lft and line <= nums[lft]:
                lft -= 1
            while rit < n and line <= nums[rit]:
                rit += 1
            ans = max(ans, line * (rit - lft - 1))
        return ans
