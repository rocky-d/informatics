from onlinejudge.leetcode import *


class Solution:
    def minOperations(self, k: int) -> int:
        k_isqrt = isqrt(k)
        if k == k_isqrt * k_isqrt:
            ans = k_isqrt + k_isqrt - 2
        else:
            ans = k_isqrt + ceil(k / k_isqrt) - 2
        return ans


eg_k = 5
print(Solution().minOperations(eg_k))
