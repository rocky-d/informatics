from rockyutil.leetcode import *


class Solution:
    def minimumDeletions(self, s: str) -> int:
        ans = len(s)
        a, b = [], [] if 'b' == s[0] else [0]
        for char, group in groupby(s):
            ls = a if 'a' == char else b
            ls.append(len(list(group)))
        a_sum, b_sum = sum(a), 0
        ans = min(ans, a_sum + b_sum)
        for ai, bi in zip(a, b):
            a_sum -= ai
            b_sum += bi
            ans = min(ans, a_sum + b_sum)
        return ans
