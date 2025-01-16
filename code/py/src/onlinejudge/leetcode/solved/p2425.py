from onlinejudge.leetcode import *


class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        num1 = reduce(xor, nums1)
        if 0b0 == 0b1 & len(nums2):
            num1 ^= num1
        num2 = reduce(xor, nums2)
        if 0b0 == 0b1 & len(nums1):
            num2 ^= num2
        return num1 ^ num2
