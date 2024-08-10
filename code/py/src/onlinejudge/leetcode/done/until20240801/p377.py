from onlinejudge.leetcode import *


class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        nums.sort()
        dp = [1] + [0 for _ in range(target)]
        for i in range(1, 1 + target):
            for num in nums:
                if num <= i:
                    dp[i] += dp[i - num]
                else:
                    break
        return dp[-1]


eg_nums = [1, 2, 3]
eg_target = 4
print(Solution().combinationSum4(eg_nums, eg_target))
