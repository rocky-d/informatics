from onlinejudge.leetcode import *


class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        k -= 1
        prefs = list(accumulate((0 if nums[i - 1] + 1 == nums[i] else 1 for i in range(1, n)), initial = 0))
        return [nums[i] if 0 == prefs[i] - prefs[i - k] else -1 for i in range(k, n)]


eg_nums = [1, 2, 3, 4, 3, 2, 5]
eg_k = 3
print(Solution().resultsArray(eg_nums, eg_k))
