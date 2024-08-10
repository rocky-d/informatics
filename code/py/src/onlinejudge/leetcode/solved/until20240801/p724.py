from onlinejudge.leetcode import *


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        pref = 0
        for i, num in enumerate(nums):
            if total == num + pref * 2:
                ans = i
                break
            pref += num
        else:
            ans = -1
        return ans
