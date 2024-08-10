from onlinejudge.leetcode import *


class Solution:
    def longestPalindrome(self, s: str) -> int:
        ans = 0
        odd = False
        for cnt in Counter(s).values():
            ans += cnt
            if 0b1 == 0b1 & cnt:
                ans -= 1
                odd = True
        if odd:
            ans += 1
        return ans
