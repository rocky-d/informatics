from rockyutil.leetcode import *


class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        max_len, max_len_cnt = 0, 0
        dp = []
        for i, nums_i in enumerate(nums):
            dp.append([1, 1])
            for j, nums_j in enumerate(nums[:i]):
                if nums_j < nums_i:
                    new_dp_j_0 = dp[j][0] + 1
                    if new_dp_j_0 == dp[-1][0]:
                        dp[-1][1] += dp[j][1]
                    elif new_dp_j_0 > dp[-1][0]:
                        dp[-1][0], dp[-1][1] = new_dp_j_0, dp[j][1]
            if max_len == dp[-1][0]:
                max_len_cnt += dp[-1][1]
            elif max_len < dp[-1][0]:
                max_len, max_len_cnt = dp[-1][0], dp[-1][1]
        return max_len_cnt


sol = Solution()

eg_nums = [1, 3, 5, 4, 7]
print(sol.findNumberOfLIS(nums = eg_nums))
