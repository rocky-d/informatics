from rockyutil.leetcode import *


class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        prefs = list(accumulate(nums, initial = 0))
        return sum(sorted(prefs[hi] - prefs[lo] for lo in range(n) for hi in range(lo + 1, n + 1))[left - 1:right]) % 1_000_000_007
