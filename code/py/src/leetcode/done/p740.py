from leetcode.util import *


class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        nums.sort()
        index = 0
        last_num = nums[0]
        while last_num == nums[index]:
            index += 1
            if index == len(nums):
                return index * last_num
        dp = [0, index * last_num]
        cnt = 0
        curr_num = nums[index]
        for num in nums[index:]:
            if curr_num == num:
                cnt += 1
            else:
                dp.append(max(dp[-1], dp[-2] + cnt * curr_num) if last_num + 1 == curr_num else dp[-1] + cnt * curr_num)
                cnt = 1
                last_num = curr_num
                curr_num = num
        dp.append(max(dp[-1], dp[-2] + cnt * curr_num) if last_num + 1 == curr_num else dp[-1] + cnt * curr_num)
        return dp[-1]


sol = Solution()

ls = [3, 4, 2]
print(sol.deleteAndEarn(ls))
