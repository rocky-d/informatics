from rockyutil.leetcode import *


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        ans = 0
        dp = []
        for i in range(len(nums)):
            dp.append(1)
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[-1] = max(dp[-1], dp[j] + 1)
            ans = max(ans, dp[-1])
        return ans


eg_nums = [4, 10, 4, 3, 8, 9]
print(Solution().lengthOfLIS(eg_nums))
