from rockyutil.leetcode import *


class Solution:
    def smallestValue(self, n: int) -> int:
        n_lst = n + 1
        while n_lst != n:
            n_lst, n_nxt = n, 0
            for factor in range(2, isqrt(n) + 1):
                times = 0
                while 0 == n % factor:
                    n //= factor
                    times += 1
                if 0 < times:
                    n_nxt += times * factor
            if 1 < n:
                n_nxt += n
            n = n_nxt
        return n


eg_n = 4
print(Solution().smallestValue(eg_n))
