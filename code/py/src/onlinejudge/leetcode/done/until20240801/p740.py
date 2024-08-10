from onlinejudge.leetcode import *


class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        def rob(nums_: List[int]) -> int:
            first, second = 0, 0
            for num_ in nums_:
                first, second = second, max(second, first + num_)
            return second

        new_nums = []
        for num in nums:
            if num >= len(new_nums):
                new_nums += [0 for _ in range(num - len(new_nums) + 1)]
            new_nums[num] += num
        return rob(new_nums)


sol = Solution()

ls = [3, 4, 2]
print(sol.deleteAndEarn(ls))
