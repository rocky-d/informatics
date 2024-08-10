from onlinejudge.leetcode import *


class Solution:
    def countSeniors(self, details: List[str]) -> int:
        return sum(1 for detail in details if 60 < int(detail[11:13]))
