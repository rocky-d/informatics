from onlinejudge.leetcode import *


class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        lft, rit = [], []
        m = 0
        for num in nums:
            if num < pivot:
                lft.append(num)
            elif pivot < num:
                rit.append(num)
            else:
                m += 1
        return lft + [pivot] * m + rit
