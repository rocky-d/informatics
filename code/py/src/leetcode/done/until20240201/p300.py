from rockyutil.leetcode import *


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        ans = 0
        dp = []
        for i, nums_i in enumerate(nums):
            dp.append(1)
            for j, nums_j in enumerate(nums[:i]):
                if nums_j < nums_i:
                    dp[-1] = max(dp[-1], dp[j] + 1)
            ans = max(ans, dp[-1])
        return ans


sol = Solution()

eg_nums = [4, 10, 4, 3, 8, 9]
print(sol.lengthOfLIS(nums = eg_nums))
