from rockyutil.leetcode import *


class Solution:
    def nonSpecialCount(self, l: int, r: int) -> int:
        ans = r - l + 1

        def primes_before(n: int) -> Generator[int, None, None]:
            tags = [False] * 2 + [True] * n
            for num in range(2, n):
                if tags[num]:
                    yield num
                    for composite in range(num * num, n, num):
                        tags[composite] = False

        for prime in primes_before(isqrt(r) + 1):
            if l <= prime * prime <= r:
                ans -= 1
        return ans
