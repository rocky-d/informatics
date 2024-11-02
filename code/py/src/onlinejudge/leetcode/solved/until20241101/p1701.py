from onlinejudge.leetcode import *


class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        total = 0
        now = 0
        for a, t in customers:
            if now < a:
                now = a
            now += t
            total += now - a
        return total / len(customers)
