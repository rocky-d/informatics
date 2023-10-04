from leetcode.util import *


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        real_index = 0
        real_num = 10001
        for num in nums:
            if real_num != num:
                nums[real_index] = num
                real_index += 1
                real_num = num
        return real_index
