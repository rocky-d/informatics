from rockyutil.leetcode import *


class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        dp = [defaultdict(lambda: 0) for _ in range(n)]
        for i in range(n):
            for j in range(i):
                diff = nums[i] - nums[j]
                ans += dp[j][diff]
                dp[i][diff] += dp[j][diff] + 1
        return ans


eg_nums = [2, 4, 6, 8, 10]
print(Solution().numberOfArithmeticSlices(nums = eg_nums))
