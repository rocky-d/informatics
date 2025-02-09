from onlinejudge.leetcode import *


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        ans = 0
        for num, group in groupby(nums):
            for _ in range(min(2, len(list(group)))):
                nums[ans] = num
                ans += 1
        return ans
