from rockyutil.leetcode import *


class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        ans = 0
        n = len(s)
        z_ls, z_i = [i for i, c in enumerate(s) if '0' == c] + [n], 0
        for lft in range(n):
            ans += z_ls[z_i] - lft
            for zs, z_j in enumerate(range(z_i + 1, min(len(z_ls), z_i + isqrt(n - lft) + 1)), start = 1):
                ans += min(max(0, (z_ls[z_j] - lft + 1) - (zs + zs * zs)), z_ls[z_j] - z_ls[z_j - 1])
            if '0' == s[lft]:
                z_i += 1
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
