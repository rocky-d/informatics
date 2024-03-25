from rockyutil.leetcode import *


class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            while nums[nums[i] - 1] != nums[i]:
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
        return [num for i, num in enumerate(nums, 1) if i != num]


eg_nums = [4, 3, 2, 7, 8, 2, 3, 1]
print(Solution().findDuplicates(eg_nums))
