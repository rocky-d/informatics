from onlinejudge.leetcode import *


class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        cnter = Counter(nums)
        return sorted(nums, key = lambda num: (cnter[num], -num))
