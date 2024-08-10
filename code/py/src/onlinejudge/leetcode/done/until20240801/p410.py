from onlinejudge.leetcode import *


class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        m, n = k, len(nums)
        dp = [[1_000_000_001 for _ in range(1 + m)] for _ in range(1 + n)]
        dp[0][0] = 0
        for i in range(1, 1 + n):
            for j in range(1, 1 + min(i, m)):
                sum_ = 0
                for k in range(i - 1, j - 2, -1):
                    sum_ += nums[k]
                    dp[i][j] = min(dp[i][j], max(dp[k][j - 1], sum_))
        return dp[-1][-1]


eg_nums = [7, 2, 5, 10, 8]
eg_k = 2
print(Solution().splitArray(nums = eg_nums, k = eg_k))
