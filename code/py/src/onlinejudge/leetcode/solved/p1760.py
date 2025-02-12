from onlinejudge.leetcode import *


class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        return bisect_left(range(max(nums) + 1), True, lo=1, key=lambda mid: sum((num - 1) // mid for num in nums) <= maxOperations)
