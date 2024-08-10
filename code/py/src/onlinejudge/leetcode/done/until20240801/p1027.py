from onlinejudge.leetcode import *


class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        dp = [defaultdict(lambda: 1) for _ in nums]
        for i, nums_i in enumerate(nums):
            for j, nums_j in enumerate(nums[:i]):
                diff = nums_i - nums_j
                dp[i][diff] = max(dp[i][diff], dp[j][diff] + 1)
        return max([max(dict_.values()) for dict_ in dp])


sol = Solution()

eg_nums = [9, 4, 7, 2, 10]
print(sol.longestArithSeqLength(nums = eg_nums))
