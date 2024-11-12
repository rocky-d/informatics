from onlinejudge.leetcode import *


class Solution:
    def countKConstraintSubstrings(self, s: str, k: int) -> int:
        ans = 0
        for leng in range(1, 1 + len(s)):
            for lft in range(len(s) - leng + 1):
                cnt0 = s[lft : lft + leng].count('0')
                cnt1 = leng - cnt0
                if cnt0 <= k or cnt1 <= k:
                    ans += 1
        return ans
