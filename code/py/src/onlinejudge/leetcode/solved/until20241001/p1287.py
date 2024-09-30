from onlinejudge.leetcode import *


class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        last_num = -1
        quarter = len(arr) / 4
        for num in arr:
            if last_num != num:
                last_num = num
                times = 0
            times += 1
            if quarter < times:
                ans = num
                break
        return ans
