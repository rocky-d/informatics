from onlinejudge.leetcode import *


class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        return len(nums) * (len(nums) - 1) - sum(cnt * (cnt - 1) for cnt in Counter(i - num for i, num in enumerate(nums)).values()) >> 1
