from onlinejudge.leetcode import *


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = [1]
        for num in reversed(nums):
            ans.insert(0, ans[0] * num)
        ans.pop(0)
        lft = 1
        for i, num in enumerate(nums):
            ans[i] *= lft
            lft *= num
        return ans
