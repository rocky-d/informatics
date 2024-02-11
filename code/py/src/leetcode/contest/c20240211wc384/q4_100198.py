from rockyutil.leetcode import *


class Solution:
    def countMatchingSubarrays(self, nums: List[int], pattern: List[int]) -> int:
        ans = 0
        m, n = len(pattern), len(nums)
        nums_s = ''
        for i in range(1, n):
            if nums[i - 1] < nums[i]:
                nums_s += '3'
            elif nums[i - 1] == nums[i]:
                nums_s += '2'
            else:
                nums_s += '1'
        pattern_s = ''
        for p in pattern:
            pattern_s += str(p + 2)
        for i in range(1 + n - m):
            if nums_s[i:].startswith(pattern_s):
                ans += 1
        return ans


eg_nums = [1, 2, 3, 4, 5, 6]
eg_pattern = [1, 1]
print(Solution().countMatchingSubarrays(eg_nums, eg_pattern))
