from rockyutil.leetcode import *


class Solution:
    def sumIndicesWithKSetBits(self, nums: List[int], k: int) -> int:
        return sum(num for i, num in enumerate(nums) if k == bin(i)[2:].count('1'))
