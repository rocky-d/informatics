from onlinejudge.leetcode import *


class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        k -= 1
        prefs = list(accumulate((0 if nums[i - 1] + 1 == nums[i] else 1 for i in range(1, len(nums))), initial=0))
        return [nums[i] if 0 == prefs[i] - prefs[i - k] else -1 for i in range(k, len(nums))]
