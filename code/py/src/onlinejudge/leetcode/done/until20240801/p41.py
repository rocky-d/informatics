from onlinejudge.leetcode import *


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
        for i, num in enumerate(nums, 1):
            if i != num:
                ans = i
                break
        else:
            ans = n + 1
        return ans


eg_nums = [3, 4, -1, 1]
print(Solution().firstMissingPositive(eg_nums))
