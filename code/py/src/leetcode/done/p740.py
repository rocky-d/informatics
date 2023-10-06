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
        first, second = 0, index * last_num
        cnt = 0
        curr_num = nums[index]
        for num in nums[index:]:
            if curr_num == num:
                cnt += 1
            else:
                first, second = second, max(second, first + cnt * curr_num) if last_num + 1 == curr_num else second + cnt * curr_num
                cnt = 1
                last_num = curr_num
                curr_num = num
        first, second = second, max(second, first + cnt * curr_num) if last_num + 1 == curr_num else second + cnt * curr_num
        return second


sol = Solution()

ls = [3, 4, 2]
print(sol.deleteAndEarn(ls))
