from onlinejudge.leetcode import *


class Solution:
    def countMatchingSubarrays(self, nums: List[int], pattern: List[int]) -> int:
        target = ''
        for i in range(len(nums) - 1):
            target += 'A' if nums[i] < nums[i + 1] else 'B' if nums[i] == nums[i + 1] else 'C'
        patt = ''
        for index in pattern:
            patt += ['B', 'A', 'C'][index]
        return len(findall(f"(?={patt})", target))


eg_nums = [1, 2, 3, 4, 5, 6]
eg_pattern = [1, 1]
print(Solution().countMatchingSubarrays(eg_nums, eg_pattern))
