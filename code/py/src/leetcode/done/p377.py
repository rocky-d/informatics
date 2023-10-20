from leetcode.leetcode import *


class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [1] + [0 for _i in range(target)]
        for i in range(1, 1 + target):
            for num in nums:
                if num <= i:
                    dp[i] += dp[i - num]
        return dp[-1]


sol = Solution()

eg_nums = [1, 2, 3]
eg_target = 4
print(sol.combinationSum4(nums = eg_nums, target = eg_target))
