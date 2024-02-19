from rockyutil.leetcode import *


class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        def divisors(s: str) -> Set[str]:
            res = set()
            n = len(s)
            for i in range(1, 1 + n):
                if 0 == n % i:
                    divisor = s[:i]
                    for j in range(i, n, i):
                        if divisor != s[j:j + i]:
                            break
                    else:
                        res.add(divisor)
            return res

        common_divisors = divisors(s = str1) & divisors(s = str2)
        return '' if 0 == len(common_divisors) else max(common_divisors, key = len)
