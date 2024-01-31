from rockyutil.leetcode import *


class Solution:
    def getLISArray(self, nums: List[int]) -> List[int]:
        dp = [1 for _ in range(len(nums))]
        for i, nums_i in enumerate(nums):
            for j, nums_j in enumerate(nums[:i]):
                if nums_j < nums_i:
                    dp[i] = max(dp[i], dp[j] + 1)
        return dp

    def minimumMountainRemovals(self, nums: List[int]) -> int:
        max_len = 0
        for left, right in zip(self.getLISArray(nums), self.getLISArray(nums[::-1])[::-1]):
            if 1 < left and 1 < right:
                max_len = max(max_len, left + right)
        return len(nums) - (max_len - 1)


eg_nums = [2, 1, 1, 5, 6, 2, 3, 1]
print(Solution().minimumMountainRemovals(nums = eg_nums))
