from onlinejudge.leetcode import *


class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        ans = 0
        n = len(nums)
        for i in range(1, n + 1):
            cnt = 0
            for j in range(1, isqrt(n // i) + 1):
                cnt += nums[i * j * j - 1]
            ans = max(ans, cnt)
        return ans
