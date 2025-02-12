from onlinejudge.leetcode import *


class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        return bisect_left(range(max(nums) + 1), 1, lo=1, key=lambda mid: 0 if maxOperations < sum((num + mid - 1) // mid - 1 for num in nums) else 1)
