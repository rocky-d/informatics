from onlinejudge.leetcode import *


class Solution:
    def getLISArray(self, nums: List[int]) -> List[int]:
        dp = [1] * len(nums)
        for i, nums_i in enumerate(nums):
            for j, nums_j in enumerate(nums[:i]):
                if nums_j < nums_i:
                    dp[i] = max(dp[i], dp[j] + 1)
        return dp

    def minimumMountainRemovals(self, nums: List[int]) -> int:
        maxm = 0
        for lft, rit in zip(self.getLISArray(nums), self.getLISArray(nums[::-1])[::-1]):
            if 1 < lft and 1 < rit:
                maxm = max(maxm, lft + rit)
        return len(nums) - (maxm - 1)


eg_nums = [2, 1, 1, 5, 6, 2, 3, 1]
print(Solution().minimumMountainRemovals(eg_nums))
