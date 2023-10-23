from rockyutil.leetcode import *


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [(nums[0], 1)]
        for nums_i in nums[1:]:
            max_ = 0
            for dp_j in dp:
                if nums_i > dp_j[0]:
                    max_ = max(max_, dp_j[1])
            dp.append((nums_i, max_ + 1))
        return sorted(dp, key = lambda x: x[1], reverse = True)[0][1]


sol = Solution()

eg_nums = [4, 10, 4, 3, 8, 9]
print(sol.lengthOfLIS(nums = eg_nums))
