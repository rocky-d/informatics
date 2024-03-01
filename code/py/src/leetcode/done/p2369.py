from rockyutil.leetcode import *


class Solution:
    def validPartition(self, nums: List[int]) -> bool:
        dp = deque((True, False, nums[0] == nums[1]), maxlen = 3)
        for i in range(2, len(nums)):
            dp.append(dp[1] and nums[i - 1] == nums[i] or dp[0] and (nums[i - 2] == nums[i - 1] == nums[i] or -1 == nums[i - 2] - nums[i - 1] == nums[i - 1] - nums[i]))
        return dp[-1]
