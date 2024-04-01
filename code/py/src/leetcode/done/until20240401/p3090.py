from rockyutil.leetcode import *


class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        ans = 0
        n = len(s)
        cnter = Counter()
        lft, rit = 0, 0
        while rit < n:
            cnter[s[rit]] += 1
            while 2 < cnter[s[rit]]:
                cnter[s[lft]] -= 1
                lft += 1
            rit += 1
            ans = max(ans, rit - lft)
        return ans
