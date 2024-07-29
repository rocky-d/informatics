from rockyutil.leetcode import *


class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        ans = 0
        n = len(s)
        z, zi = [i for i, c in enumerate(s) if '0' == c] + [n], 0
        for lft in range(n):
            ans += z[zi] - lft
            for zs, zj in enumerate(range(zi + 1, min(len(z), zi + isqrt(n - lft) + 1)), start = 1):
                ans += min(max(0, (z[zj] - lft + 1) - (zs + zs * zs)), z[zj] - z[zj - 1])
            if '0' == s[lft]:
                zi += 1
        return ans


eg_s = '101101'
print(Solution().numberOfSubstrings(eg_s))

# 11 0111 0111 011 0

'''
1 <= n <= 40000
1 <= z+o <= n
z*z <= o

z+z*z <= n
z*(z+1) <= n
z < sqrt(n) < z+1
'''
