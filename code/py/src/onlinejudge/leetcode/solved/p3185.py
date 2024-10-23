from onlinejudge.leetcode import *


class Solution:
    def countCompleteDayPairs(self, hours: List[int]) -> int:
        cnter = [0] * 24
        for x in (hour % 24 for hour in hours):
            cnter[x] += 1
        ans = comb(cnter[0], 2) + comb(cnter[12], 2)
        for x in range(1, 12):
            ans += cnter[x] * cnter[24 - x]
        return ans
