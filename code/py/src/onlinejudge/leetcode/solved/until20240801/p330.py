from onlinejudge.leetcode import *


class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        ans = 0
        cover = 1
        idx, length = 0, len(nums)
        while cover <= n:
            if idx < length and nums[idx] <= cover:
                cover += nums[idx]
                idx += 1
            else:
                cover += cover
                ans += 1
        return ans
