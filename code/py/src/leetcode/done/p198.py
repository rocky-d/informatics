from leetcode.util import *


class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [0, nums[0]]
        for num in nums[1:]:
            dp.append(max(dp[-1], dp[-2] + num))
        return dp[-1]
