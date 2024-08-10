from onlinejudge.leetcode import *


class Solution:
    def numberOfWeeks(self, milestones: List[int]) -> int:
        maxm = max(milestones)
        lst = sum(milestones) - maxm
        return lst + min(lst + 1, maxm)
