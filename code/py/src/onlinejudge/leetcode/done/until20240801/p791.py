from onlinejudge.leetcode import *


class Solution:
    def customSortString(self, order: str, s: str) -> str:
        s_cnter = Counter(s)
        return ''.join(s_cnter[char] * char for char in order + ''.join(s_cnter.keys() - frozenset(order)))
