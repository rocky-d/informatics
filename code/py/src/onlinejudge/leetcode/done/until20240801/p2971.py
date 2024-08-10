from onlinejudge.leetcode import *


class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        pres = [0]
        for num in nums:
            pres.append(pres[-1] + num)
        for i in range(len(nums) - 1, 1, -1):
            if pres[i] > nums[i]:
                ans = pres[1 + i]
                break
        else:
            ans = -1
        return ans
