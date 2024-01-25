from rockyutil.leetcode import *


class Solution:
    def sumIndicesWithKSetBits(self, nums: List[int], k: int) -> int:
        return sum(nums[i] for i in filter(lambda i: k == bin(i)[2:].count('1'), range(len(nums))))
