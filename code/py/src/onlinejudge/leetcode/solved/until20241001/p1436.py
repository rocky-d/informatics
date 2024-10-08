from onlinejudge.leetcode import *


class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        a_set, b_set = set(), set()
        for a, b in paths:
            a_set.add(a)
            b_set.add(b)
        return tuple(b_set - a_set)[0]
