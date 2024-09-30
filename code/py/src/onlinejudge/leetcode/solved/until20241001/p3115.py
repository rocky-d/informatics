from onlinejudge.leetcode import *


class Solution:
    def maximumPrimeDifference(self, nums: List[int]) -> int:
        is_composite = [True] * 2 + [False] * 99
        for num in range(2, 101):
            if not is_composite[num]:
                for composite in range(num * num, 101, num):
                    is_composite[composite] = True
        lft = 0
        while is_composite[nums[lft]]:
            lft += 1
        rit = len(nums) - 1
        while is_composite[nums[rit]]:
            rit -= 1
        return rit - lft
