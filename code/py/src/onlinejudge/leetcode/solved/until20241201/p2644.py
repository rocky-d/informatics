from onlinejudge.leetcode import *


class Solution:
    def maxDivScore(self, nums: List[int], divisors: List[int]) -> int:
        ans = 1_000_000_001
        maxm = 0
        for divisor in divisors:
            cnt = 0
            for num in nums:
                if 0 == num % divisor:
                    cnt += 1
            if maxm < cnt:
                maxm = cnt
                ans = divisor
            elif maxm == cnt:
                ans = min(ans, divisor)
        return ans
