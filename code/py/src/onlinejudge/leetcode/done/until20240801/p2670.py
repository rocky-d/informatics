from onlinejudge.leetcode import *


class Solution:
    def distinctDifferenceArray(self, nums: List[int]) -> List[int]:
        left_diffs = []
        nums_set = set()
        for num in nums:
            nums_set.add(num)
            left_diffs.append(len(nums_set))
        right_diffs = []
        nums_set = set()
        for num in reversed(nums):
            right_diffs.insert(0, len(nums_set))
            nums_set.add(num)
        return [left_diff - right_diff for left_diff, right_diff in zip(left_diffs, right_diffs)]


eg_nums = [3, 2, 3, 4, 2]
print(Solution().distinctDifferenceArray(nums = eg_nums))
