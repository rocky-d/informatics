from onlinejudge.leetcode import *


class Solution:
    def returnToBoundaryCount(self, nums: List[int]) -> int:
        ans = 0
        position = 0
        for num in nums:
            position_last = position
            position += num
            if 0 != position_last and 0 == position:
                ans += 1
        return ans
