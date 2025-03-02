from onlinejudge.leetcode import *


class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        quarter = len(arr) / 4
        lst = -1
        for num in arr:
            if lst != num:
                lst = num
                times = 0
            times += 1
            if quarter < times:
                ans = num
                break
        return ans
