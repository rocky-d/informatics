from onlinejudge.leetcode import *


class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        ans = 0
        n = len(s)
        z, zi = [i for i, c in enumerate(s) if '0' == c] + [n], 0
        for lft in range(n):
            ans += z[zi] - lft + sum(min(max(0, (z[zj] - lft + 1) - (zs + zs * zs)), z[zj] - z[zj - 1]) for zs, zj in enumerate(range(zi + 1, min(len(z), zi + isqrt(n - lft) + 1)), start = 1))
            if '0' == s[lft]:
                zi += 1
        return ans


eg_s = '101101'
print(Solution().numberOfSubstrings(eg_s))
