from rockyutil.leetcode import *


class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        dp = [nums[0]]
        for i in range(1, len(nums)):
            dp.append(max(dp[-min(i, k):]) + nums[i])
        return dp[-1]


eg_nums = [10, -5, -2, 4, 0, 3]
eg_k = 3
print(Solution().maxResult(eg_nums, eg_k))
