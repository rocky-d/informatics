from rockyutil.leetcode import *


class Solution:
    def countMatchingSubarrays(self, nums: List[int], pattern: List[int]) -> int:
        m, n = len(pattern), len(nums)
        f1 = lambda a, b: a < b
        f2 = lambda a, b: a == b
        f3 = lambda a, b: a > b
        dp = [True for _ in range(n)]
        for i in range(m):
            dp_last, dp = dp, []
            f = f1 if 1 == pattern[i] else f2 if 0 == pattern[i] else f3
            for j in range(n - i - 1):
                dp.append(True if dp_last[j] and f(nums[j + i], nums[j + i + 1]) else False)
        return dp.count(True)


eg_nums = [1, 2, 3, 4, 5, 6]
eg_pattern = [1, 1]
print(Solution().countMatchingSubarrays(eg_nums, eg_pattern))
