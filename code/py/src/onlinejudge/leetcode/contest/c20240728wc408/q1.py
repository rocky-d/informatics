from onlinejudge.leetcode import *


class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:
        total = sum(nums)
        cnt1 = sum(num for num in nums if num <= 9)
        cnt2 = sum(num for num in nums if 10 <= num)
        return cnt1 > total - cnt1 or cnt2 > total - cnt2
