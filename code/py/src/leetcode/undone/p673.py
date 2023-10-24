from rockyutil.leetcode import *


class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        dp = [[nums[0], 1, 1]]
        for nums_i in nums[1:]:
            max_, cnt = 0, 0
            for dp_j in dp:
                if nums_i > dp_j[0]:
                    if dp_j[1] > max_:
                        max_, cnt = dp_j[1], 1
                    # elif dp_j[1] == max_:
                    #     cnt += 1
                elif nums_i == dp_j[1]:
                    dp_j[2] += 1
            dp.append([nums_i, max_ + 1, cnt])
        print(dp)


sol = Solution()

eg_nums = [1,3,5,4,7]
print(sol.findNumberOfLIS(nums = eg_nums))
