from rockyutil.leetcode import *


class Solution:
    def countMatchingSubarrays(self, nums: List[int], pattern: List[int]) -> int:
        m, n = len(pattern), len(nums)
        dp = [True for _ in range(n)]
        for i in range(m):
            dp_last, dp = dp, []
            f = (lambda a, b: a < b) if 1 == pattern[i] else (lambda a, b: a == b) if 0 == pattern[i] else (lambda a, b: a > b)
            for j in range(n - i - 1):
                dp.append(True if dp_last[j] and f(nums[j + i], nums[j + i + 1]) else False)
        return dp.count(True)


eg_nums = [1, 2, 3, 4, 5, 6]
eg_pattern = [1, 1]
print(Solution().countMatchingSubarrays(eg_nums, eg_pattern))
