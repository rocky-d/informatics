from onlinejudge.leetcode import *


class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        maxm = 1
        i, n = 0, len(nums)
        while i < n:
            j = i
            ones = nums[j].bit_count()
            while i < n and ones == nums[i].bit_count():
                i += 1
            block = nums[j:i]
            if maxm <= min(block):
                maxm = max(block)
            else:
                ans = False
                break
        else:
            ans = True
        return ans
