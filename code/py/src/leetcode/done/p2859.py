from rockyutil.leetcode import *


class Solution:
    def sumIndicesWithKSetBits(self, nums: List[int], k: int) -> int:
        ans = 0
        for i, num in enumerate(nums):
            if k == bin(i)[2:].count('1'):
                ans += num
        return ans
