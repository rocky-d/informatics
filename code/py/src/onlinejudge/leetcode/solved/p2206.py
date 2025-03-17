from onlinejudge.leetcode import *


class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        return all(0b0 == 0b1 & cnt for cnt in Counter(nums).values())
